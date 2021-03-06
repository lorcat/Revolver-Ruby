# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_motor_widget.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setEnabled(True)
        Form.resize(998, 40)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(800, 30))
        Form.setMaximumSize(QtCore.QSize(16777215, 40))
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.stackedWidget = QtGui.QStackedWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.ok_page = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_page.sizePolicy().hasHeightForWidth())
        self.ok_page.setSizePolicy(sizePolicy)
        self.ok_page.setMinimumSize(QtCore.QSize(0, 30))
        self.ok_page.setObjectName(_fromUtf8("ok_page"))
        self.gridLayout = QtGui.QGridLayout(self.ok_page)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.motor_controls = QtGui.QWidget(self.ok_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.motor_controls.sizePolicy().hasHeightForWidth())
        self.motor_controls.setSizePolicy(sizePolicy)
        self.motor_controls.setMinimumSize(QtCore.QSize(0, 0))
        self.motor_controls.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.motor_controls.setObjectName(_fromUtf8("motor_controls"))
        self.gridLayout_2 = QtGui.QGridLayout(self.motor_controls)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.button_change_position_minus_double = QtGui.QPushButton(self.motor_controls)
        self.button_change_position_minus_double.setMinimumSize(QtCore.QSize(40, 27))
        self.button_change_position_minus_double.setMaximumSize(QtCore.QSize(40, 27))
        self.button_change_position_minus_double.setObjectName(_fromUtf8("button_change_position_minus_double"))
        self.gridLayout_2.addWidget(self.button_change_position_minus_double, 0, 2, 1, 1)
        self.button_change_position_plus = QtGui.QPushButton(self.motor_controls)
        self.button_change_position_plus.setMinimumSize(QtCore.QSize(40, 27))
        self.button_change_position_plus.setMaximumSize(QtCore.QSize(40, 27))
        self.button_change_position_plus.setObjectName(_fromUtf8("button_change_position_plus"))
        self.gridLayout_2.addWidget(self.button_change_position_plus, 0, 7, 1, 1)
        self.button_change_position_minus = QtGui.QPushButton(self.motor_controls)
        self.button_change_position_minus.setMinimumSize(QtCore.QSize(40, 27))
        self.button_change_position_minus.setMaximumSize(QtCore.QSize(40, 27))
        self.button_change_position_minus.setObjectName(_fromUtf8("button_change_position_minus"))
        self.gridLayout_2.addWidget(self.button_change_position_minus, 0, 3, 1, 1)
        self.button_change_position_plus_double = QtGui.QPushButton(self.motor_controls)
        self.button_change_position_plus_double.setMinimumSize(QtCore.QSize(40, 27))
        self.button_change_position_plus_double.setMaximumSize(QtCore.QSize(40, 27))
        self.button_change_position_plus_double.setObjectName(_fromUtf8("button_change_position_plus_double"))
        self.gridLayout_2.addWidget(self.button_change_position_plus_double, 0, 9, 1, 1)
        self.motor_position = QtGui.QDoubleSpinBox(self.motor_controls)
        self.motor_position.setMinimumSize(QtCore.QSize(100, 27))
        self.motor_position.setMaximumSize(QtCore.QSize(150, 27))
        self.motor_position.setToolTip(_fromUtf8(""))
        self.motor_position.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.motor_position.setDecimals(5)
        self.motor_position.setMaximum(99999.0)
        self.motor_position.setSingleStep(0.1)
        self.motor_position.setObjectName(_fromUtf8("motor_position"))
        self.gridLayout_2.addWidget(self.motor_position, 0, 5, 1, 1)
        self.gridLayout.addWidget(self.motor_controls, 0, 0, 1, 1)
        self.button_stop_all_moves = QtGui.QPushButton(self.ok_page)
        self.button_stop_all_moves.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_stop_all_moves.sizePolicy().hasHeightForWidth())
        self.button_stop_all_moves.setSizePolicy(sizePolicy)
        self.button_stop_all_moves.setMinimumSize(QtCore.QSize(100, 27))
        self.button_stop_all_moves.setMaximumSize(QtCore.QSize(120, 27))
        self.button_stop_all_moves.setStyleSheet(_fromUtf8("QPushButton{background:purple;font-weight:bold;color:#fff;}\n"
"QPushButton:disabled{ background:silver;color:grey }"))
        self.button_stop_all_moves.setObjectName(_fromUtf8("button_stop_all_moves"))
        self.gridLayout.addWidget(self.button_stop_all_moves, 0, 6, 1, 1)
        self.label_2 = QtGui.QLabel(self.ok_page)
        self.label_2.setMinimumSize(QtCore.QSize(70, 0))
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.button_refresh = QtGui.QPushButton(self.ok_page)
        self.button_refresh.setMinimumSize(QtCore.QSize(30, 27))
        self.button_refresh.setMaximumSize(QtCore.QSize(27, 16777215))
        self.button_refresh.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/devices/icons/ic_refresh_black_48dp.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.button_refresh.setIcon(icon)
        self.button_refresh.setObjectName(_fromUtf8("button_refresh"))
        self.gridLayout.addWidget(self.button_refresh, 0, 4, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 7, 1, 1)
        self.step_size = QtGui.QDoubleSpinBox(self.ok_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.step_size.sizePolicy().hasHeightForWidth())
        self.step_size.setSizePolicy(sizePolicy)
        self.step_size.setMinimumSize(QtCore.QSize(80, 27))
        self.step_size.setMaximumSize(QtCore.QSize(120, 27))
        self.step_size.setDecimals(5)
        self.step_size.setMinimum(1e-05)
        self.step_size.setMaximum(999.0)
        self.step_size.setSingleStep(0.1)
        self.step_size.setProperty("value", 0.1)
        self.step_size.setObjectName(_fromUtf8("step_size"))
        self.gridLayout.addWidget(self.step_size, 0, 2, 1, 1)
        self.buttonSettings = QtGui.QPushButton(self.ok_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSettings.sizePolicy().hasHeightForWidth())
        self.buttonSettings.setSizePolicy(sizePolicy)
        self.buttonSettings.setMinimumSize(QtCore.QSize(40, 27))
        self.buttonSettings.setMaximumSize(QtCore.QSize(40, 27))
        self.buttonSettings.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/devices/icons/ic_settings_black_48dp.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.buttonSettings.setIcon(icon1)
        self.buttonSettings.setIconSize(QtCore.QSize(19, 19))
        self.buttonSettings.setObjectName(_fromUtf8("buttonSettings"))
        self.gridLayout.addWidget(self.buttonSettings, 0, 5, 1, 1)
        self.button_zero = QtGui.QPushButton(self.ok_page)
        self.button_zero.setMinimumSize(QtCore.QSize(30, 27))
        self.button_zero.setMaximumSize(QtCore.QSize(30, 16777215))
        self.button_zero.setObjectName(_fromUtf8("button_zero"))
        self.gridLayout.addWidget(self.button_zero, 0, 3, 1, 1)
        self.stackedWidget.addWidget(self.ok_page)
        self.error_tab = QtGui.QWidget()
        self.error_tab.setStyleSheet(_fromUtf8("background:red"))
        self.error_tab.setObjectName(_fromUtf8("error_tab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.error_tab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label = QtGui.QLabel(self.error_tab)
        self.label.setStyleSheet(_fromUtf8("font-weight:bold"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.error_tab)
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.button_change_position_plus, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.action_change_motor_position_plus)
        QtCore.QObject.connect(self.button_change_position_minus, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.action_change_motor_position_minus)
        QtCore.QObject.connect(self.button_change_position_plus_double, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.action_change_motor_position_plus_double)
        QtCore.QObject.connect(self.button_change_position_minus_double, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.action_change_motor_position_minus_double)
        QtCore.QObject.connect(self.buttonSettings, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.action_show_settings_window)
        QtCore.QObject.connect(self.button_stop_all_moves, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.action_stop_motor)
        QtCore.QObject.connect(self.step_size, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), Form.action_change_step)
        QtCore.QObject.connect(self.button_zero, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.action_change_motor_position_zero)
        QtCore.QObject.connect(self.step_size, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), Form.action_step_menu)
        QtCore.QObject.connect(self.button_refresh, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.action_change_motor)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.button_change_position_minus_double, self.button_change_position_minus)
        Form.setTabOrder(self.button_change_position_minus, self.motor_position)
        Form.setTabOrder(self.motor_position, self.button_change_position_plus)
        Form.setTabOrder(self.button_change_position_plus, self.button_change_position_plus_double)
        Form.setTabOrder(self.button_change_position_plus_double, self.step_size)
        Form.setTabOrder(self.step_size, self.buttonSettings)
        Form.setTabOrder(self.buttonSettings, self.button_stop_all_moves)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Motor widget", None))
        self.button_change_position_minus_double.setToolTip(_translate("Form", "Decrease position by (step size * 10)", None))
        self.button_change_position_minus_double.setText(_translate("Form", "<<", None))
        self.button_change_position_plus.setToolTip(_translate("Form", "Increase position by step size", None))
        self.button_change_position_plus.setText(_translate("Form", ">", None))
        self.button_change_position_minus.setToolTip(_translate("Form", "Decrease position by step size", None))
        self.button_change_position_minus.setText(_translate("Form", "<", None))
        self.button_change_position_plus_double.setToolTip(_translate("Form", "Increase position by (step size * 10)", None))
        self.button_change_position_plus_double.setText(_translate("Form", ">>", None))
        self.button_stop_all_moves.setToolTip(_translate("Form", "Stop motor", None))
        self.button_stop_all_moves.setText(_translate("Form", "Stop motor", None))
        self.label_2.setText(_translate("Form", "step size:", None))
        self.button_refresh.setToolTip(_translate("Form", "Refresh motor info (limits, position)", None))
        self.buttonSettings.setToolTip(_translate("Form", "Show attributes editor", None))
        self.button_zero.setToolTip(_translate("Form", "Move motor to zero position", None))
        self.button_zero.setText(_translate("Form", "&0", None))
        self.label.setText(_translate("Form", "ERROR", None))

import resources_rc
