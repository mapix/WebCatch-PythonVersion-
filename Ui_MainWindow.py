# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\PYWS\WebCatch\WebCatch-PythonVersion-\MainWindow.ui'
#
# Created: Wed Nov 12 12:49:43 2014
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1032, 564)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("_eric4project/ico.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 531, 25))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.leURL = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.leURL.setObjectName(_fromUtf8("leURL"))
        self.horizontalLayout.addWidget(self.leURL)
        self.btnExct = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnExct.setObjectName(_fromUtf8("btnExct"))
        self.horizontalLayout.addWidget(self.btnExct)
        self.teExctData = QtGui.QTextEdit(Dialog)
        self.teExctData.setGeometry(QtCore.QRect(20, 70, 531, 241))
        self.teExctData.setObjectName(_fromUtf8("teExctData"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(570, 110, 191, 31))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_7 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.lePort = QtGui.QLineEdit(self.horizontalLayoutWidget_3)
        self.lePort.setObjectName(_fromUtf8("lePort"))
        self.horizontalLayout_3.addWidget(self.lePort)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(570, 50, 191, 31))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.leUsername = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.leUsername.setObjectName(_fromUtf8("leUsername"))
        self.horizontalLayout_2.addWidget(self.leUsername)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(570, 80, 191, 31))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lePassword = QtGui.QLineEdit(self.horizontalLayoutWidget_4)
        self.lePassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lePassword.setObjectName(_fromUtf8("lePassword"))
        self.horizontalLayout_4.addWidget(self.lePassword)
        self.horizontalLayoutWidget_5 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(570, 140, 191, 31))
        self.horizontalLayoutWidget_5.setObjectName(_fromUtf8("horizontalLayoutWidget_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_6 = QtGui.QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        self.leDBName = QtGui.QLineEdit(self.horizontalLayoutWidget_5)
        self.leDBName.setObjectName(_fromUtf8("leDBName"))
        self.horizontalLayout_5.addWidget(self.leDBName)
        self.horizontalLayoutWidget_6 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(570, 20, 191, 31))
        self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_6)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_6)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_6.addWidget(self.label_2)
        self.leHost = QtGui.QLineEdit(self.horizontalLayoutWidget_6)
        self.leHost.setObjectName(_fromUtf8("leHost"))
        self.horizontalLayout_6.addWidget(self.leHost)
        self.btnConnect = QtGui.QPushButton(Dialog)
        self.btnConnect.setGeometry(QtCore.QRect(570, 200, 91, 23))
        self.btnConnect.setObjectName(_fromUtf8("btnConnect"))
        self.btnSave = QtGui.QPushButton(Dialog)
        self.btnSave.setGeometry(QtCore.QRect(800, 60, 211, 21))
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.horizontalLayoutWidget_7 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(560, 170, 231, 31))
        self.horizontalLayoutWidget_7.setObjectName(_fromUtf8("horizontalLayoutWidget_7"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_8 = QtGui.QLabel(self.horizontalLayoutWidget_7)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_7.addWidget(self.label_8)
        self.lbState = QtGui.QLabel(self.horizontalLayoutWidget_7)
        self.lbState.setObjectName(_fromUtf8("lbState"))
        self.horizontalLayout_7.addWidget(self.lbState)
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 50, 111, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.leTablename = QtGui.QLineEdit(Dialog)
        self.leTablename.setGeometry(QtCore.QRect(890, 90, 71, 20))
        self.leTablename.setObjectName(_fromUtf8("leTablename"))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(820, 90, 71, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(20, 330, 781, 231))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.horizontalLayoutWidget_8 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(560, 220, 221, 31))
        self.horizontalLayoutWidget_8.setObjectName(_fromUtf8("horizontalLayoutWidget_8"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_9 = QtGui.QLabel(self.horizontalLayoutWidget_8)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_8.addWidget(self.label_9)
        self.lineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget_8)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_8.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget_8)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_8.addWidget(self.pushButton)
        self.horizontalLayoutWidget_9 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(560, 250, 221, 31))
        self.horizontalLayoutWidget_9.setObjectName(_fromUtf8("horizontalLayoutWidget_9"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_12 = QtGui.QLabel(self.horizontalLayoutWidget_9)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_9.addWidget(self.label_12)
        self.lineEdit_2 = QtGui.QLineEdit(self.horizontalLayoutWidget_9)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_9.addWidget(self.lineEdit_2)
        self.pushButton_4 = QtGui.QPushButton(self.horizontalLayoutWidget_9)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_9.addWidget(self.pushButton_4)
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 290, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 290, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.btnLoad = QtGui.QPushButton(Dialog)
        self.btnLoad.setGeometry(QtCore.QRect(800, 120, 211, 21))
        self.btnLoad.setObjectName(_fromUtf8("btnLoad"))
        self.teHTMLCode = QtGui.QTextEdit(Dialog)
        self.teHTMLCode.setGeometry(QtCore.QRect(820, 180, 201, 141))
        self.teHTMLCode.setObjectName(_fromUtf8("teHTMLCode"))
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(820, 160, 61, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.btnExtfromCode = QtGui.QPushButton(Dialog)
        self.btnExtfromCode.setGeometry(QtCore.QRect(820, 320, 201, 21))
        self.btnExtfromCode.setObjectName(_fromUtf8("btnExtfromCode"))
        self.leThreshold = QtGui.QLineEdit(Dialog)
        self.leThreshold.setGeometry(QtCore.QRect(330, 50, 113, 20))
        self.leThreshold.setObjectName(_fromUtf8("leThreshold"))
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(183, 50, 141, 20))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.btnDisConnect = QtGui.QPushButton(Dialog)
        self.btnDisConnect.setGeometry(QtCore.QRect(670, 200, 91, 23))
        self.btnDisConnect.setObjectName(_fromUtf8("btnDisConnect"))
        self.horizontalLayoutWidget_10 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(790, 20, 231, 31))
        self.horizontalLayoutWidget_10.setObjectName(_fromUtf8("horizontalLayoutWidget_10"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setMargin(0)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_17 = QtGui.QLabel(self.horizontalLayoutWidget_10)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_10.addWidget(self.label_17)
        self.leCurTableName = QtGui.QLineEdit(self.horizontalLayoutWidget_10)
        self.leCurTableName.setObjectName(_fromUtf8("leCurTableName"))
        self.horizontalLayout_10.addWidget(self.leCurTableName)
        self.btnChangeTName = QtGui.QPushButton(self.horizontalLayoutWidget_10)
        self.btnChangeTName.setObjectName(_fromUtf8("btnChangeTName"))
        self.horizontalLayout_10.addWidget(self.btnChangeTName)
        self.btnCloseCurTab = QtGui.QPushButton(Dialog)
        self.btnCloseCurTab.setGeometry(QtCore.QRect(710, 320, 75, 23))
        self.btnCloseCurTab.setObjectName(_fromUtf8("btnCloseCurTab"))
        self.btnShowTables = QtGui.QPushButton(Dialog)
        self.btnShowTables.setGeometry(QtCore.QRect(830, 360, 181, 23))
        self.btnShowTables.setObjectName(_fromUtf8("btnShowTables"))
        self.teTables = QtGui.QTextEdit(Dialog)
        self.teTables.setGeometry(QtCore.QRect(830, 410, 181, 71))
        self.teTables.setObjectName(_fromUtf8("teTables"))
        self.label_18 = QtGui.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(830, 390, 61, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.leDTableName = QtGui.QLineEdit(Dialog)
        self.leDTableName.setGeometry(QtCore.QRect(900, 490, 101, 20))
        self.leDTableName.setObjectName(_fromUtf8("leDTableName"))
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(830, 490, 61, 20))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.btnDeleteTable = QtGui.QPushButton(Dialog)
        self.btnDeleteTable.setGeometry(QtCore.QRect(830, 520, 171, 23))
        self.btnDeleteTable.setObjectName(_fromUtf8("btnDeleteTable"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "WebExtraction v0.3 beta by 血与光辉@HIT", None))
        self.label.setText(_translate("Dialog", "URL:", None))
        self.leURL.setText(_translate("Dialog", "http://www.converse.com.cn/men.htm?iid=tpnvm0912001&source=topnav", None))
        self.btnExct.setText(_translate("Dialog", "Extract", None))
        self.label_7.setText(_translate("Dialog", "PORT:", None))
        self.lePort.setText(_translate("Dialog", "3306", None))
        self.label_4.setText(_translate("Dialog", "UserName:", None))
        self.leUsername.setText(_translate("Dialog", "root", None))
        self.label_5.setText(_translate("Dialog", "PassWord:", None))
        self.lePassword.setText(_translate("Dialog", "6191162", None))
        self.label_6.setText(_translate("Dialog", "DBName:", None))
        self.leDBName.setText(_translate("Dialog", "test", None))
        self.label_3.setText(_translate("Dialog", "Host:", None))
        self.leHost.setText(_translate("Dialog", "localhost", None))
        self.btnConnect.setText(_translate("Dialog", "Connect", None))
        self.btnSave.setText(_translate("Dialog", "Save the Data into Mysql", None))
        self.label_8.setText(_translate("Dialog", "MYSQL Connection State:", None))
        self.lbState.setText(_translate("Dialog", "Unconnected", None))
        self.label_10.setText(_translate("Dialog", "Console:", None))
        self.leTablename.setText(_translate("Dialog", "table0", None))
        self.label_11.setText(_translate("Dialog", "TableName:", None))
        self.label_9.setText(_translate("Dialog", "Row Id:", None))
        self.pushButton.setText(_translate("Dialog", "Delete", None))
        self.label_12.setText(_translate("Dialog", "Col Id:", None))
        self.pushButton_4.setText(_translate("Dialog", "Delete", None))
        self.pushButton_2.setText(_translate("Dialog", "AddRow", None))
        self.pushButton_3.setText(_translate("Dialog", "AddCol", None))
        self.btnLoad.setText(_translate("Dialog", "Load the Data from Mysql", None))
        self.label_15.setText(_translate("Dialog", "HTML Code:", None))
        self.btnExtfromCode.setText(_translate("Dialog", "Extract from HTMLCode", None))
        self.leThreshold.setText(_translate("Dialog", "10", None))
        self.label_16.setText(_translate("Dialog", "threshold(minval is 0):", None))
        self.btnDisConnect.setText(_translate("Dialog", "DisConnect", None))
        self.label_17.setText(_translate("Dialog", "CurTableName:", None))
        self.btnChangeTName.setText(_translate("Dialog", "Change", None))
        self.btnCloseCurTab.setText(_translate("Dialog", "CloseCurTab", None))
        self.btnShowTables.setText(_translate("Dialog", "Show Tables", None))
        self.label_18.setText(_translate("Dialog", "Tables:", None))
        self.label_13.setText(_translate("Dialog", "TableName:", None))
        self.btnDeleteTable.setText(_translate("Dialog", "Delete Table", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

