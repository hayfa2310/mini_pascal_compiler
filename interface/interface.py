# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_compilateur.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import compile_icon_rc
import open_icon_rc
import save_icon_rc

from line_numbers import QCodeEditor


class Ui_Compilateur(object):
    def setupUi(self, Compilateur):
        Compilateur.setObjectName("Compilateur")
        Compilateur.setEnabled(True)
        Compilateur.resize(499, 596)
        self.groupBox = QtWidgets.QGroupBox(Compilateur)
        self.groupBox.setGeometry(QtCore.QRect(20, 80, 461, 71))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 341, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(360, 30, 91, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/open-file-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 101, 16))
        self.label_5.setObjectName("label_5")
        self.plainTextEdit_2 = QCodeEditor(Compilateur)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(20, 190, 461, 161))
        self.plainTextEdit_2.zoomIn(1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Compilateur)
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 420, 461, 91))
        self.plainTextEdit.setStyleSheet("background-color: rgb(49, 49, 49);\n""color: rgb(255, 0, 0);")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.zoomIn(1)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.groupBox_3 = QtWidgets.QGroupBox(Compilateur)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 530, 461, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 20, 91, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 20, 231, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 20, 101, 23))
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Compilateur)
        self.label.setGeometry(QtCore.QRect(20, 10, 451, 41))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Compilateur)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 360, 101, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/code-coding-compile-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(Compilateur)
        self.label_7.setGeometry(QtCore.QRect(20, 170, 121, 16))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Compilateur)
        QtCore.QMetaObject.connectSlotsByName(Compilateur)

    def retranslateUi(self, Compilateur):
        _translate = QtCore.QCoreApplication.translate
        Compilateur.setWindowTitle(_translate("Compilateur", "Dialog"))
        self.groupBox.setTitle(_translate("Compilateur", "Importer le fichier source"))
        self.pushButton.setText(_translate("Compilateur", "Parcourir.."))
        self.label_5.setText(_translate("Compilateur", "<html><head/><body><p><span style=\" font-weight:600;\">Code Source</span></p><p><br/></p></body></html>"))
        self.groupBox_3.setTitle(_translate("Compilateur", "Enregistrer Trace dans un fichier"))
        self.pushButton_4.setText(_translate("Compilateur", "Enregistrer"))
        self.pushButton_3.setText(_translate("Compilateur", "Parcourir.."))
        self.label.setText(_translate("Compilateur", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">Compilateur Mini-Pascal</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Compilateur", "Compiler"))
        self.label_7.setText(_translate("Compilateur", "<html><head/><body><p><span style=\" font-weight:600;\">Code Source</span></p><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Compilateur = QtWidgets.QDialog()
    ui = Ui_Compilateur()
    ui.setupUi(Compilateur)
    Compilateur.show()
    sys.exit(app.exec_())

