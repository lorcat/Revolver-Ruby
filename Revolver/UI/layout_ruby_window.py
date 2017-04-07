# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_ruby_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(824, 686)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_motors = QtGui.QWidget()
        self.tab_motors.setObjectName(_fromUtf8("tab_motors"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_motors)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.wdgt_zoom = QtGui.QWidget(self.tab_motors)
        self.wdgt_zoom.setMinimumSize(QtCore.QSize(100, 50))
        self.wdgt_zoom.setObjectName(_fromUtf8("wdgt_zoom"))
        self.gridLayout_6 = QtGui.QGridLayout(self.wdgt_zoom)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.pushButton = QtGui.QPushButton(self.wdgt_zoom)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_6.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.wdgt_zoom)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_6.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.wdgt_zoom, 0, 2, 1, 1)
        self.wdgt_diacorr = QtGui.QWidget(self.tab_motors)
        self.wdgt_diacorr.setMinimumSize(QtCore.QSize(100, 50))
        self.wdgt_diacorr.setObjectName(_fromUtf8("wdgt_diacorr"))
        self.gridLayout_5 = QtGui.QGridLayout(self.wdgt_diacorr)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_2.addWidget(self.wdgt_diacorr, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.wdgt_motors = QtGui.QWidget(self.tab_motors)
        self.wdgt_motors.setMinimumSize(QtCore.QSize(0, 50))
        self.wdgt_motors.setObjectName(_fromUtf8("wdgt_motors"))
        self.gridLayout_7 = QtGui.QGridLayout(self.wdgt_motors)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_2.addWidget(self.wdgt_motors, 1, 0, 1, 3)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_motors, _fromUtf8(""))
        self.tab_calc = QtGui.QWidget()
        self.tab_calc.setObjectName(_fromUtf8("tab_calc"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_calc)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.wv_calc = QtWebKit.QWebView(self.tab_calc)
        self.wv_calc.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.wv_calc.setObjectName(_fromUtf8("wv_calc"))
        self.gridLayout_3.addWidget(self.wv_calc, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_calc, _fromUtf8(""))
        self.tab_save = QtGui.QWidget()
        self.tab_save.setObjectName(_fromUtf8("tab_save"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_save)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.wv_save = QtWebKit.QWebView(self.tab_save)
        self.wv_save.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.wv_save.setObjectName(_fromUtf8("wv_save"))
        self.gridLayout_4.addWidget(self.wv_save, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_save, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuCalibration = QtGui.QMenu(self.menubar)
        self.menuCalibration.setObjectName(_fromUtf8("menuCalibration"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionCalibrate_Motors = QtGui.QAction(MainWindow)
        self.actionCalibrate_Motors.setObjectName(_fromUtf8("actionCalibrate_Motors"))
        self.menuCalibration.addAction(self.actionCalibrate_Motors)
        self.menubar.addAction(self.menuCalibration.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.actionZoomOut)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.actionZoomIn)
        QtCore.QObject.connect(self.menubar, QtCore.SIGNAL(_fromUtf8("triggered(QAction*)")), MainWindow.processMenuAction)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setToolTip(_translate("MainWindow", "Zoom out to have larger field of view", None))
        self.pushButton.setText(_translate("MainWindow", "Zoom Out", None))
        self.pushButton_2.setToolTip(_translate("MainWindow", "Zoom in to measure Ruby signal and copy positions to the beamline", None))
        self.pushButton_2.setText(_translate("MainWindow", "Zoom In", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_motors), _translate("MainWindow", "Motors", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_calc), _translate("MainWindow", "Calculations", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_save), _translate("MainWindow", "Saving Positions", None))
        self.menuCalibration.setTitle(_translate("MainWindow", "Expert", None))
        self.actionCalibrate_Motors.setText(_translate("MainWindow", "Calibrate Motors", None))

from PyQt4 import QtWebKit
