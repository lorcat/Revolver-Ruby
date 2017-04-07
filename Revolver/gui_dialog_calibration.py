from PyQt4 import QtCore, QtGui

from Revolver.common import Tester
from Revolver.classes import devices
from Revolver.runnables import getPool, DoorRunner
from Revolver.pytango import getMotorPosition

from Revolver.UI.layout_dialog_calibration import Ui_Dialog



class CalibrationDialog(QtGui.QDialog, Tester, Ui_Dialog):
    # key for motors
    RBX = "RBX"
    RBY = "RBY"
    RBZ = "RBZ"

    # door
    DOOR = "haspllabcl1.desy.de:10000/llab/door/haspllabcl1.01"

    def __init__(self, parent=None):
        Tester.__init__(self)
        super(CalibrationDialog, self).__init__(parent=parent)

        self.setupUi(self)

        self.debug("Initialization of the calibration dialog")

        self._thread_pool = getPool(parent=self)

        # get motor positions and set the corresponding spin boxes
        key = self.RBX
        spinbox = self.dsb_rbx
        value = getMotorPosition(devices.DEVICE_PATHS[key])
        if self.testFloat(value):
            spinbox.setValue(value)

        key = self.RBY
        spinbox = self.dsb_rby
        value = getMotorPosition(devices.DEVICE_PATHS[key])
        if self.testFloat(value):
            spinbox.setValue(value)

        key = self.RBZ
        spinbox = self.dsb_rbz
        value = getMotorPosition(devices.DEVICE_PATHS[key])
        if self.testFloat(value):
            spinbox.setValue(value)

    def calibrate(self, motor, value):
        """
        Calibrates a motor via Sardana
        @return:
        """
        self.debug("Calibrating a motor ({}) to the value ({})".format(motor, value))
        cmdline = "{} calibrate {} {}".format(self.DOOR, motor, value)
        self.parent().jsRunMacro(cmdline)

    def actionSetRBX(self):
        """
        Calibrates rbx motor
        @return:
        """
        motor = self.RBX.lower()
        value = self.dsb_rbx.value()
        self.calibrate(motor, value)

    def actionSetRBY(self):
        """
        Calibrates rby motor
        @return:
        """
        motor = self.RBY.lower()
        value = self.dsb_rby.value()
        self.calibrate(motor, value)

    def actionSetRBZ(self):
        """
        Calibrates rbz motor
        @return:
        """
        motor = self.RBZ.lower()
        value = self.dsb_rbz.value()
        self.calibrate(motor, value)
        
    def actionRBXzero(self):
        """
        Calibrates rbx motor to zero
        @return:
        """
        motor = self.RBX.lower()
        self.calibrate(motor, 0.)

    def actionRBYzero(self):
        """
        Calibrates rby motor to zero
        @return:
        """
        motor = self.RBY.lower()
        self.calibrate(motor, 0.)

    def actionRBZzero(self):
        """
        Calibrates rbz motor to zero
        @return:
        """
        motor = self.RBZ.lower()
        self.calibrate(motor, 0.)