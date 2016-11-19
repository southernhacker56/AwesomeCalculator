import sys
import constants
from PyQt4 import QtCore, QtGui
from awesome_calculator_layout import Ui_Form



class CalculatorApp(QtGui.QWidget):
    result = 0
    prevInput = 0
    
    def __init__(self):
        super(CalculatorApp, self).__init__()        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.set_event_clicked()
            
    def set_event_clicked(self):
        # numerical values
        self.ui.number0Button.clicked.connect(lambda: self.print_value(constants.BUTTON_ZERO_VALUE))
        self.ui.number1Button.clicked.connect(lambda: self.print_value(constants.BUTTON_ONE_VALUE))
        self.ui.number2Button.clicked.connect(lambda: self.print_value(constants.BUTTON_TWO_VALUE))
        self.ui.number3Button.clicked.connect(lambda: self.print_value(constants.BUTTON_THREE_VALUE))
        self.ui.number4Button.clicked.connect(lambda: self.print_value(constants.BUTTON_FOUR_VALUE))
        self.ui.number5Button.clicked.connect(lambda: self.print_value(constants.BUTTON_FIVE_VALUE))
        self.ui.number6Button.clicked.connect(lambda: self.print_value(constants.BUTTON_SIX_VALUE))
        self.ui.number7Button.clicked.connect(lambda: self.print_value(constants.BUTTON_SEVEN_VALUE))
        self.ui.number8Button.clicked.connect(lambda: self.print_value(constants.BUTTON_EIGHT_VALUE))
        self.ui.number9Button.clicked.connect(lambda: self.print_value(constants.BUTTON_NINE_VAULE))

    def print_value(self,value):
        self.ui.displayScreen.setText(str(value))
        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())