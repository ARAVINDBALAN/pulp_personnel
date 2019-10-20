# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scheduler_main.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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

class Ui_Scheduler(object):
    def setupUi(self, Scheduler):
        Scheduler.setObjectName(_fromUtf8("Scheduler"))
        Scheduler.resize(986, 689)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../.designer/backup/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Scheduler.setWindowIcon(icon)
        self.modify_sku = QtGui.QPushButton(Scheduler)
        self.modify_sku.setGeometry(QtCore.QRect(680, 110, 211, 29))
        self.modify_sku.setStyleSheet(_fromUtf8("font: 9pt \"MS Shell Dlg 2\";"))
        self.modify_sku.setObjectName(_fromUtf8("modify_sku"))
        self.line = QtGui.QFrame(Scheduler)
        self.line.setGeometry(QtCore.QRect(580, 70, 20, 571))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.path = QtGui.QLineEdit(Scheduler)
        self.path.setGeometry(QtCore.QRect(60, 40, 261, 29))
        self.path.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.path.setObjectName(_fromUtf8("path"))
        self.Browse = QtGui.QPushButton(Scheduler)
        self.Browse.setGeometry(QtCore.QRect(340, 40, 100, 29))
        self.Browse.setStyleSheet(_fromUtf8("selection-color: rgb(0, 0, 255);\n"
"font: 9pt \"MS Shell Dlg 2\";"))
        self.Browse.setObjectName(_fromUtf8("Browse"))
        self.modify_machine = QtGui.QPushButton(Scheduler)
        self.modify_machine.setGeometry(QtCore.QRect(680, 170, 211, 29))
        self.modify_machine.setStyleSheet(_fromUtf8("font: 9pt \"MS Shell Dlg 2\";"))
        self.modify_machine.setObjectName(_fromUtf8("modify_machine"))
        self.next = QtGui.QPushButton(Scheduler)
        self.next.setGeometry(QtCore.QRect(380, 610, 181, 29))
        self.next.setStyleSheet(_fromUtf8("font: 9pt \"MS Shell Dlg 2\";\n"
"font: 75 9pt \"MS Shell Dlg 2\";"))
        self.next.setObjectName(_fromUtf8("next"))
        self.calendarWidget = QtGui.QCalendarWidget(Scheduler)
        self.calendarWidget.setGeometry(QtCore.QRect(60, 350, 448, 174))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.label = QtGui.QLabel(Scheduler)
        self.label.setGeometry(QtCore.QRect(110, 550, 261, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.date = QtGui.QLabel(Scheduler)
        self.date.setGeometry(QtCore.QRect(860, 20, 141, 20))
        self.date.setObjectName(_fromUtf8("date"))
        self.day = QtGui.QLabel(Scheduler)
        self.day.setGeometry(QtCore.QRect(860, 40, 141, 20))
        self.day.setObjectName(_fromUtf8("day"))
        self.browse_check = QtGui.QCheckBox(Scheduler)
        self.browse_check.setGeometry(QtCore.QRect(30, 40, 21, 31))
        self.browse_check.setText(_fromUtf8(""))
        self.browse_check.setObjectName(_fromUtf8("browse_check"))
        self.browse_check_2 = QtGui.QCheckBox(Scheduler)
        self.browse_check_2.setGeometry(QtCore.QRect(380, 550, 96, 20))
        self.browse_check_2.setText(_fromUtf8(""))
        self.browse_check_2.setObjectName(_fromUtf8("browse_check_2"))
        self.confirm_date = QtGui.QPushButton(Scheduler)
        self.confirm_date.setGeometry(QtCore.QRect(610, 550, 161, 29))
        self.confirm_date.setStyleSheet(_fromUtf8("font: 9pt \"MS Shell Dlg 2\";"))
        self.confirm_date.setObjectName(_fromUtf8("confirm_date"))
        self.label_2 = QtGui.QLabel(Scheduler)
        self.label_2.setGeometry(QtCore.QRect(610, 330, 201, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.datelistview = QtGui.QListWidget(Scheduler)
        self.datelistview.setGeometry(QtCore.QRect(610, 370, 341, 159))
        self.datelistview.setObjectName(_fromUtf8("datelistview"))
        self.datedeletebutton = QtGui.QPushButton(Scheduler)
        self.datedeletebutton.setGeometry(QtCore.QRect(790, 550, 161, 29))
        self.datedeletebutton.setStyleSheet(_fromUtf8("font: 9pt \"MS Shell Dlg 2\";"))
        self.datedeletebutton.setObjectName(_fromUtf8("datedeletebutton"))
        self.label_3 = QtGui.QLabel(Scheduler)
        self.label_3.setGeometry(QtCore.QRect(20, 650, 111, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Scheduler)
        self.label_4.setGeometry(QtCore.QRect(70, 10, 281, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.inputskudimension = QtGui.QPushButton(Scheduler)
        self.inputskudimension.setGeometry(QtCore.QRect(60, 100, 261, 29))
        self.inputskudimension.setStyleSheet(_fromUtf8("font: 9pt \"MS Shell Dlg 2\";"))
        self.inputskudimension.setObjectName(_fromUtf8("inputskudimension"))
        self.get_sku_format = QtGui.QPushButton(Scheduler)
        self.get_sku_format.setGeometry(QtCore.QRect(60, 160, 261, 41))
        self.get_sku_format.setStyleSheet(_fromUtf8("font: 75 9pt \"MS Shell Dlg 2\";"))
        self.get_sku_format.setObjectName(_fromUtf8("get_sku_format"))
        self.proceedtonexttext = QtGui.QLabel(Scheduler)
        self.proceedtonexttext.setGeometry(QtCore.QRect(60, 220, 311, 41))
        self.proceedtonexttext.setObjectName(_fromUtf8("proceedtonexttext"))
        self.label_5 = QtGui.QLabel(Scheduler)
        self.label_5.setGeometry(QtCore.QRect(250, 310, 121, 31))
        self.label_5.setStyleSheet(_fromUtf8("font: 75 12pt \"Roboto\";\n"
"text-decoration: underline;"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.show_calc_ten = QtGui.QPushButton(Scheduler)
        self.show_calc_ten.setGeometry(QtCore.QRect(680, 230, 211, 29))
        self.show_calc_ten.setStyleSheet(_fromUtf8("font: 9pt \"MS Shell Dlg 2\";"))
        self.show_calc_ten.setObjectName(_fromUtf8("show_calc_ten"))

        self.retranslateUi(Scheduler)
        QtCore.QMetaObject.connectSlotsByName(Scheduler)

    def retranslateUi(self, Scheduler):
        Scheduler.setWindowTitle(_translate("Scheduler", "Scheduler Application for PULP", None))
        self.modify_sku.setText(_translate("Scheduler", "Add/Modify  SKUs", None))
        self.Browse.setText(_translate("Scheduler", "Browse", None))
        self.modify_machine.setText(_translate("Scheduler", "Add/Modify Machine Config", None))
        self.next.setText(_translate("Scheduler", "Next", None))
        self.label.setText(_translate("Scheduler", "Select working days from the calender", None))
        self.date.setText(_translate("Scheduler", "TextLabel", None))
        self.day.setText(_translate("Scheduler", "TextLabel", None))
        self.confirm_date.setText(_translate("Scheduler", "Confirm date", None))
        self.label_2.setText(_translate("Scheduler", "Selected days for scheduling", None))
        self.datedeletebutton.setText(_translate("Scheduler", "Delete selected days", None))
        self.label_3.setText(_translate("Scheduler", "@lpha Version", None))
        self.label_4.setText(_translate("Scheduler", "Input KM Tracker file here ", None))
        self.inputskudimension.setText(_translate("Scheduler", "Input SKU dimension", None))
        self.get_sku_format.setText(_translate("Scheduler", "Generate formatted input from KM", None))
        self.proceedtonexttext.setText(_translate("Scheduler", "Output generted from KM Tracker and \n"
"Sku Dimension , proceed to \"Next\" ", None))
        self.label_5.setText(_translate("Scheduler", "CALENDER", None))
        self.show_calc_ten.setText(_translate("Scheduler", "Show Calculated Tenative", None))

