# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'awesome_calculator_layout.ui'
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
        Form.resize(341, 352)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStatusTip(_fromUtf8(""))
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(_fromUtf8("background-color: #696969;"))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.displayScreen = QtGui.QTextBrowser(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayScreen.sizePolicy().hasHeightForWidth())
        self.displayScreen.setSizePolicy(sizePolicy)
        self.displayScreen.setAutoFillBackground(False)
        self.displayScreen.setFrameShape(QtGui.QFrame.WinPanel)
        self.displayScreen.setFrameShadow(QtGui.QFrame.Plain)
        self.displayScreen.setObjectName(_fromUtf8("displayScreen"))
        self.verticalLayout.addWidget(self.displayScreen)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, -1, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.number9Button = QtGui.QPushButton(Form)
        self.number9Button.setStyleSheet(_fromUtf8("background-color: #F0FFF0;\n"
"font: 75 oblique 20pt \"DejaVu Sans\";"))
        self.number9Button.setObjectName(_fromUtf8("number9Button"))
        self.gridLayout.addWidget(self.number9Button, 3, 4, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(Form)
        self.pushButton_11.setStyleSheet(_fromUtf8("background-color: #F0FFF0;;\n"
"font: 75 oblique 20pt \"DejaVu Sans\";"))
        self.pushButton_11.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_11.setAutoDefault(False)
        self.pushButton_11.setDefault(False)
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.gridLayout.addWidget(self.pushButton_11, 6, 4, 1, 1)
        self.number6Button = QtGui.QPushButton(Form)
        self.number6Button.setStyleSheet(_fromUtf8("background-color: #F0FFF0;;\n"
"font: 75 oblique 20pt \"DejaVu Sans\";"))
        self.number6Button.setObjectName(_fromUtf8("number6Button"))
        self.gridLayout.addWidget(self.number6Button, 4, 4, 1, 1)
        self.number2Button = QtGui.QPushButton(Form)
        self.number2Button.setStyleSheet(_fromUtf8("background-color: #F0FFF0;;\n"
"font: 75 oblique 20pt \"DejaVu Sans\";"))
        self.number2Button.setObjectName(_fromUtf8("number2Button"))
        self.gridLayout.addWidget(self.number2Button, 5, 3, 1, 1)
        self.solutionButton = QtGui.QPushButton(Form)
        self.solutionButton.setStyleSheet(_fromUtf8("background-color: #F0FFF0;;\n"
"font: 75 oblique 20pt \"DejaVu Sans\";"))
        self.solutionButton.setObjectName(_fromUtf8("solutionButton"))
        self.gridLayout.addWidget(self.solutionButton, 6, 5, 1, 1)
        self.clearButton = QtGui.QPushButton(Form)
        self.clearButton.setStyleSheet(_fromUtf8("background-color: #F0FFF0;\n"
"font: 75 oblique 20pt \"DejaVu Sans\";"))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.gridLayout.addWidget(self.clearButton, 2, 2, 1, 1)
        self.number3Button = QtGui.QPushButton(Form)
        self.number3Button.setStyleSheet(_fromUtf8("background-color: #F0FFF0;;\n"
"font: 75 oblique 20pt \"DejaVu Sans\";"))
        self.number3Button.setObjectName(_fromUtf8("number3Button"))
        self.gridLayout.addWidget(self.number3Button, 5, 4, 1, 1)
        self.number5Button = QtGui.QPushButton(Form)
        self.number5Button.setStyleSheet(_fromUtf8("font: 75 20pt \"Cantarell\";background-color: #F0FFF0;"))
        self.number5Button.setObjectName(_fromUtf8("number5Button"))
        self.gridLayout.addWidget(self.number5Button, 4, 3, 1, 1)
        self.number8Button = QtGui.QPushButton(Form)
        self.number8Button.setBaseSize(QtCore.QSize(0, 0))
        self.number8Button.setStyleSheet(_fromUtf8("background-color: #F0FFF0;\n"
"font: 75 oblique 20pt \"DejaVu Sans\";"))
        self.number8Button.setObjectName(_fromUtf8("number8Button"))
        self.gridLayout.addWidget(self.number8Button, 3, 3, 1, 1)
        self.divisonButton = QtGui.QPushButton(Form)
        self.divisonButton.setStyleSheet(_fromUtf8("background-color: #F0FFF0;\n"
"font: 75 oblique 20pt \"DejaVu Sans\";"))
        self.divisonButton.setObjectName(_fromUtf8("divisonButton"))
        self.gridLayout.addWidget(self.divisonButton, 2, 4, 1, 1)
        self.number0Button = QtGui.QPushButton(Form)
        self.number0Button.setStyleSheet(_fromUtf8("background-color: #F0FFF0;;\n"
"font: 75 oblique 20pt \"DejaVu Sans\";"))
        self.number0Button.setObjectName(_fromUtf8("number0Button"))
        self.gridLayout.addWidget(self.number0Button, 6, 2, 1, 2)
        self.number7Button = QtGui.QPushButton(Form)
        self.number7Button.setStyleSheet(_fromUtf8("background-color: #F0FFF0;\n"
"font: 75 oblique 20pt \"DejaVu Sans\";"))
        self.number7Button.setObjectName(_fromUtf8("number7Button"))
        self.gridLayout.addWidget(self.number7Button, 3, 2, 1, 1)
        self.number4Button = QtGui.QPushButton(Form)
        self.number4Button.setStyleSheet(_fromUtf8("background-color: #F0FFF0;\n"
"font: 75 oblique 20pt \"DejaVu Sans\";"))
        self.number4Button.setObjectName(_fromUtf8("number4Button"))
        self.gridLayout.addWidget(self.number4Button, 4, 2, 1, 1)
        self.number1Button = QtGui.QPushButton(Form)
        self.number1Button.setStyleSheet(_fromUtf8("background-color: #F0FFF0;;\n"
"font: 75 oblique 20pt \"DejaVu Sans\";"))
        self.number1Button.setCheckable(False)
        self.number1Button.setChecked(False)
        self.number1Button.setAutoDefault(False)
        self.number1Button.setObjectName(_fromUtf8("number1Button"))
        self.gridLayout.addWidget(self.number1Button, 5, 2, 1, 1)
        self.multiplicationButton = QtGui.QPushButton(Form)
        self.multiplicationButton.setBaseSize(QtCore.QSize(0, 0))
        self.multiplicationButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.multiplicationButton.setStyleSheet(_fromUtf8("background-color: #F0FFF0;\n"
"font: 75 oblique 20pt \"DejaVu Sans\";"))
        self.multiplicationButton.setObjectName(_fromUtf8("multiplicationButton"))
        self.gridLayout.addWidget(self.multiplicationButton, 2, 5, 1, 1)
        self.subtractionButton = QtGui.QPushButton(Form)
        self.subtractionButton.setStyleSheet(_fromUtf8("background-color: #F0FFF0;;\n"
"font: 75 oblique 20pt \"DejaVu Sans\";"))
        self.subtractionButton.setObjectName(_fromUtf8("subtractionButton"))
        self.gridLayout.addWidget(self.subtractionButton, 3, 5, 1, 1)
        self.additionButton = QtGui.QPushButton(Form)
        self.additionButton.setStyleSheet(_fromUtf8("background-color: #F0FFF0;;\n"
"font: 75 oblique 20pt \"DejaVu Sans\";"))
        self.additionButton.setObjectName(_fromUtf8("additionButton"))
        self.gridLayout.addWidget(self.additionButton, 4, 5, 1, 1)
        self.percentButton = QtGui.QPushButton(Form)
        self.percentButton.setStyleSheet(_fromUtf8("background-color: #F0FFF0;\n"
"font: 75 oblique 20pt \"DejaVu Sans\";"))
        self.percentButton.setObjectName(_fromUtf8("percentButton"))
        self.gridLayout.addWidget(self.percentButton, 5, 5, 1, 1)
        self.inverseButton = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.inverseButton.setFont(font)
        self.inverseButton.setStyleSheet(_fromUtf8("background-color: #F0FFF0;\n"
"font: 75 oblique 20pt \"DejaVu Sans\";"))
        self.inverseButton.setObjectName(_fromUtf8("inverseButton"))
        self.gridLayout.addWidget(self.inverseButton, 2, 3, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Awesome Calculator", None))
        self.displayScreen.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.number9Button.setText(_translate("Form", "9", None))
        self.pushButton_11.setText(_translate("Form", ".", None))
        self.number6Button.setText(_translate("Form", "6", None))
        self.number2Button.setText(_translate("Form", "2", None))
        self.solutionButton.setText(_translate("Form", "=", None))
        self.clearButton.setText(_translate("Form", "C", None))
        self.number3Button.setText(_translate("Form", "3", None))
        self.number5Button.setText(_translate("Form", "5", None))
        self.number8Button.setText(_translate("Form", "8", None))
        self.divisonButton.setText(_translate("Form", "/", None))
        self.number0Button.setText(_translate("Form", "0", None))
        self.number7Button.setText(_translate("Form", "7", None))
        self.number4Button.setText(_translate("Form", "4", None))
        self.number1Button.setText(_translate("Form", "1", None))
        self.multiplicationButton.setText(_translate("Form", "x", None))
        self.subtractionButton.setText(_translate("Form", "-", None))
        self.additionButton.setText(_translate("Form", "+", None))
        self.percentButton.setText(_translate("Form", "%", None))
        self.inverseButton.setText(_translate("Form", "+/-", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

