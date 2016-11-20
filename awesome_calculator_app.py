import sys
import constants
from PyQt4 import QtCore, QtGui
from awesome_calculator_layout import Ui_Form


class CalculatorApp(QtGui.QWidget):
    nResult = 0
    nPrevInputNumVal= constants.NO_PRE_INPUT_NUM_VALUE
    nValue1 = 0
    nValue2 = 0
    

    def __init__(self):
        super(CalculatorApp, self).__init__()        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.set_event_clicked()
            
    def set_event_clicked(self):
        # numerical
        self.ui.number0Button.clicked.connect(lambda: self.numerical_input_handle())
        self.ui.number1Button.clicked.connect(lambda: self.numerical_input_handle())
        self.ui.number2Button.clicked.connect(lambda: self.numerical_input_handle())
        self.ui.number3Button.clicked.connect(lambda: self.numerical_input_handle())
        self.ui.number4Button.clicked.connect(lambda: self.numerical_input_handle())
        self.ui.number5Button.clicked.connect(lambda: self.numerical_input_handle())
        self.ui.number6Button.clicked.connect(lambda: self.numerical_input_handle())
        self.ui.number7Button.clicked.connect(lambda: self.numerical_input_handle())
        self.ui.number8Button.clicked.connect(lambda: self.numerical_input_handle())
        self.ui.number9Button.clicked.connect(lambda: self.numerical_input_handle())
        
        # math operation
        self.ui.additionButton.clicked.connect(lambda: self.operation_handle())
        self.ui.subtractionButton.clicked.connect(lambda: self.operation_handle())
        self.ui.multiplicationButton.clicked.connect(lambda: self.operation_handle())
        self.ui.divisonButton.clicked.connect(lambda: self.operation_handle())
        self.ui.solutionButton.clicked.connect(lambda: self.operation_handle())
        
        #TODO Add precent(reminder), decimal place, and inverse,
        
        
        # clear operation
        self.ui.clearButton.clicked.connect(lambda:self.clear())

    def print_value(self,value):
        self.ui.displayScreen.setText(str(value))
    
    
    def numerical_input_handle(self):
        inputValue = self.sender().text()

        if(self.nPrevInputNumVal != constants.NO_PRE_INPUT_NUM_VALUE):
            self.print_value(str(self.nPrevInputNumVal) + str(inputValue))
            self.nPrevInputNumVal = int(str(self.nPrevInputNumVal) + str(inputValue))
        else:
            self.nPrevInputNumVal = int(inputValue)
            self.print_value(str(inputValue))
            

    '''
    Determine the desire operation based on the
    button press and previous input field
    '''
    def operation_handle(self):
        
        self.print_value("Testing")
    
    
    '''
    Preform the operation, based on the action button
    '''
    def preform_operation(self):
        return 0
    
    '''
    Clear the display screen and reset the result value to zero.
    '''
    def clear(self):
        self.nResult = 0
        self.nPrevInputNumVal= constants.NO_PRE_INPUT_NUM_VALUE
        self.ui.displayScreen.setText("")
    
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())