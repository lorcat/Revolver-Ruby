from PyQt4 import QtCore, QtGui

from Revolver.common import Tester
from Revolver.classes import devices
from Revolver.gui_stacked_motors_controls_widget import StackedMotorControls

from Revolver.config.keys import *
import Revolver.config.config_global as config

from Revolver.runnables import getPool, DoorRunner, LambdaRunner
from Revolver.pytango import getMotorPosition, setMotorPosition

from Revolver.gui_dialog_calibration import CalibrationDialog

from Revolver.UI.layout_ruby_window import Ui_MainWindow

from Revolver.gui_diamond_correction import DiamondCorrectionWidget

# fill the information on the devices
P02_DEVICES = dict((x, config.DEVICE_SERVER_P02  + y) for x, y in config.DEVICE_NAMES.iteritems())
devices.DEVICE_NAMES = dict((y, x) for x, y in config.DEVICE_NAMES.iteritems())
devices.DEVICE_PATHS = P02_DEVICES

class RubyWindow(QtGui.QMainWindow, Tester, Ui_MainWindow):

    WINDOW_TITLE = "Offline Ruby system"

    # keys to work with for QSettings
    WIN_SIZE = "size"
    WIN_POS = "position"

    # JS template to send result of operation back
    JS_MACRO_TMPL = "ExtQt.processMacroResponse(%DATAOUT%, %DATAINFO%, %DATAERR%);"

    JS_MACRO_SUBSTOUT = "%DATAOUT%"
    JS_MACRO_SUBSTINFO = "%DATAINFO%"
    JS_MACRO_SUBSTERR = "%DATAERR%"

    # templates to look for and substitute motor positions
    JS_MOTX = "%MOTX%"
    JS_MOTY = "%MOTY%"
    JS_MOTZ = "%MOTZ%"

    # key for motors
    RBX = "RBX"
    RBY = "RBY"
    RBZ = "RBZ"
    RBZOOM = "RBZOOM"

    def __init__(self):
        super(RubyWindow, self).__init__()
        Tester.__init__(self)

        self.debug("Initializin main window")

        self.__init_variables()
        self.__init_gui()
        self.__init_events()

        self.readSettings()
        self.show()

    def __init_variables(self):
        self.debug("Init variables")

        # motors widget
        self.motors = None

        # widget with diamond correction
        self.diacorr = None

        # tread pool
        self._thread_pool = getPool(parent=self)

    def __init_gui(self):
        self.debug("Initializing gui")

        # create elements
        self.setupUi(self)

        # adding diamond correction widget
        self.addDiamondCorrection()

        # add motor widgets
        self.addMotors()

        # html - for calculations
        self.initializeCalculationsHtml()
        # html for position saving
        self.initializePositionsHtml()

        # window title
        self.setWindowTitle(self.WINDOW_TITLE)

    def __init_events(self):
        self.debug("Initializing qt events for main window")

    def addMotors(self):
        """
        Loading motor names, adding the devices to the gui
        @return:
        """

        motors = [
                P02_DEVICES["RBX"],
                P02_DEVICES["RBY"],
                P02_DEVICES["RBZ"],
                P02_DEVICES["RBZOOM"]
            ]

        self.motors = StackedMotorControls(parent=self, motors=motors, title="Microscope Motors")
        self.wdgt_motors.layout().addWidget(self.motors)

    def addDiamondCorrection(self):
        """
        Adding a widget with diamond correction
        @return:
        """
        self.diacorr = DiamondCorrectionWidget(parent=self)
        self.wdgt_diacorr.layout().addWidget(self.diacorr)

    def initializeCalculationsHtml(self):
        """
        Initialize calculations part
        @return:
        """
        fn = config.HTML[HTML_CALC_PATH]
        self.debug("Setting calculations HTML page ({})".format(fn))

        url = QtCore.QUrl()
        url.setPath(fn)

        frame = self.wv_calc.page().mainFrame()
        self.connect(frame, QtCore.SIGNAL("javaScriptWindowObjectCleared()"), self.processReloadCalcHtmlPage)
        self.connect(self.wv_calc, QtCore.SIGNAL("loadFinished (bool)"), self.processReloadCalcHtmlPage)
        self.wv_calc.setUrl(url)

    def initializePositionsHtml(self):
        """
        Initialize calculations part
        @return:
        """
        fn = config.HTML[HTML_POS_PATH]
        self.debug("Setting positions HTML page ({})".format(fn))

        url = QtCore.QUrl()
        url.setPath(fn)

        frame = self.wv_save.page().mainFrame()
        self.connect(frame, QtCore.SIGNAL("javaScriptWindowObjectCleared()"), self.processReloadPosSaveHtmlPage)
        self.connect(self.wv_save, QtCore.SIGNAL("loadFinished (bool)"), self.processReloadPosSaveHtmlPage)
        self.wv_save.setUrl(url)

    @QtCore.pyqtSlot()
    def processReloadCalcHtmlPage(self, *args):
        """
        Processes events on html page reload for indicator page - adds an javascript object
        :return:
        """
        self.wv_calc.page().mainFrame().addToJavaScriptWindowObject("qtWindow", self)

    @QtCore.pyqtSlot()
    def processReloadPosSaveHtmlPage(self, *args):
        """
        Processes events on html page reload for indicator page - adds an javascript object
        :return:
        """
        self.wv_save.page().mainFrame().addToJavaScriptWindowObject("qtWindow", self)

    @QtCore.pyqtSlot()
    def jsTest(self):
        """
        Simple test demonstrating communication of HTML+JS with Qt
        @return:
        """
        QtGui.QMessageBox.information(self, "Greetings from JS", "Test fired by JS script")
        self.info("size and position ({}, {})".format( self.size(), self.pos()))

    def readSettings(self):
        """
        Reads settings from registry
        @return:
        """
        self.debug("Reading settings")
        settings = QtCore.QSettings()

        size = settings.value(self.WIN_SIZE, QtCore.QSize(*config.DEFAULT_WINDOW_SIZE))
        pos = settings.value(self.WIN_POS, QtCore.QPoint(*config.DEFAULT_WINDOW_POS))

        self.move(pos)
        self.resize(size)
        self.settings = settings


    def writeSettings(self):
        """
        Writing settings for position and size
        @return:
        """
        self.debug("Writing settings")
        self.settings.setValue(self.WIN_SIZE, self.size())
        self.settings.setValue(self.WIN_POS, self.pos())

    def closeEvent(self, event):
        """
        Cleanup during the close event
        @param args:
        @param kwargs:
        @return:
        """
        self.debug("Closing the window")
        self.writeSettings()
        event.accept()

    @QtCore.pyqtSlot(str)
    def jsRunMacro(self, cmdline):
        """
        Takes the macro parameter from the HTML+JS and run it
        @return:
        """
        self.debug("Tryting to run macro ({})".format(cmdline))

        args = cmdline.split(" ")
        door = args.pop(0)

        # get rid of empty arguments
        tmp_args = []
        for (i, el) in enumerate(args):

            key = self.RBX
            if el == self.JS_MOTX:
                pos = getMotorPosition(devices.DEVICE_PATHS[key])
                if self.testFloat(pos):
                    el = "{:.4f}".format(getMotorPosition(devices.DEVICE_PATHS[key]))
                else:
                    return

            key = self.RBY
            if el == self.JS_MOTY:
                pos = getMotorPosition(devices.DEVICE_PATHS[key])
                if self.testFloat(pos):
                    el = "{:.4f}".format(getMotorPosition(devices.DEVICE_PATHS[key]))
                else:
                    return

            key = self.RBZ
            if el == self.JS_MOTZ:
                pos = getMotorPosition(devices.DEVICE_PATHS[key])
                if self.testFloat(pos):
                    el = "{:.4f}".format(getMotorPosition(devices.DEVICE_PATHS[key]))
                else:
                    return

            if len(el)>0:
                tmp_args.append(el)

        self.debug("Final command for the door ({}) is ({})".format(door, tmp_args))

        runner = DoorRunner(door, tmp_args, response_func=self.jsResponseMacro)
        self._thread_pool.tryStart(runner)

    @QtCore.pyqtSlot(str)
    def jsResponseMacro(self, *args):
        """
        Takes the response from the macro server and output it fith some filtering
        @return:
        """
        self.debug("Receiving response from the macro server door ({})".format(args))

        # get all - info+error are colored
        output, info, error = args

        if not self.test(output,list) and not self.test(output, tuple):
            output = [output]

        if not self.test(info, list) and not self.test(info, tuple):
            info = [info]

        if not self.test(error, list) and not self.test(error, tuple):
            error = [error]

        tmpl = self.JS_MACRO_TMPL.replace(self.JS_MACRO_SUBSTOUT, str(list(output)))
        self.debug("Template: {}".format(tmpl))
        tmpl = tmpl.replace(self.JS_MACRO_SUBSTINFO, str(list(info)))
        self.debug("Template: {}".format(tmpl))
        tmpl = tmpl.replace(self.JS_MACRO_SUBSTERR, str(list(error)))
        self.debug("Template: {}".format(tmpl))

        self.debug("Executing Javascript: ({});\n".format(tmpl))

        self.wv_save.page().mainFrame().evaluateJavaScript(tmpl)
        self.wv_save.update()

    @QtCore.pyqtSlot()
    def actionZoomIn(self):
        """
        Performs a zoom in action, stops the motor before moving
        @return:
        """
        self.debug("Performing a zoom in action")

        func = lambda dp=devices.DEVICE_PATHS[self.RBZOOM]: setMotorPosition(dp, 100.)
        runner = LambdaRunner(func)

        self._thread_pool.tryStart(runner)

    @QtCore.pyqtSlot()
    def actionZoomOut(self):
        """
        Performs a zoom out action, stops the motor before moving
        @return:
        """
        self.debug("Performing a zoom out action")

        func = lambda dp=devices.DEVICE_PATHS[self.RBZOOM]: setMotorPosition(dp, 0.)
        runner = LambdaRunner(func)

        self._thread_pool.tryStart(runner)

    @QtCore.pyqtSlot(object)
    def processMenuAction(self, action):
        """
        Processing actions of the main menu
        @param action:
        @return:
        """
        self.debug("Processing menu action ({})".format(action))

        if "calibrate" in str(action.text()).lower():
            dialog = CalibrationDialog(parent=self)
            dialog.exec_()