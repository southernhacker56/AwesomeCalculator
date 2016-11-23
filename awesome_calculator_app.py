import sys
import constants
from PyQt4 import QtCore, QtGui
from awesome_calculator_layout import Ui_Form


# Calculator Application
class CalculatorApp(QtGui.QWidget):
    # Private member for the Calculator App
    b_result_is_value1 = False
    n_display_value = constants.NUMBER_VALUE_NONE
    n_value1 = constants.NUMBER_VALUE_NONE
    n_value2 = constants.NUMBER_VALUE_NONE
    s_operation = constants.NO_OPERATION_VALUE

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
        self.ui.solutionButton.clicked.connect(
            lambda: self.preform_operation(self.n_value1, self.n_value2, self.s_operation))
        self.ui.inverseButton.clicked.connect(lambda: self.inverse_display_value())

        # TODO Add percent, decimal place

        # clear operation
        self.ui.clearButton.clicked.connect(lambda: self.clear())

    def print_value(self):
        self.ui.displayScreen.setText(str(self.n_display_value))

    # Handle the numerical value
    def numerical_input_handle(self):
        if self.b_result_is_value1:
            return

        n_input_value = self.sender().text()

        # If the previous button press was a number button, then just append the numerical
        # value at the end of the previous inputted values
        if self.n_display_value is not constants.NUMBER_VALUE_NONE:
            self.n_display_value = float(str(int(self.n_display_value)) + str(int(n_input_value)))
            self.print_value()
        else:
            self.n_display_value = float(n_input_value)
            self.print_value()

        if self.n_value1 is not constants.NUMBER_VALUE_NONE:
            self.n_value2 = self.n_display_value

    # Determine the desire operation based on the
    # button press and previous input field
    def operation_handle(self):
        if self.b_result_is_value1:
            self.b_result_is_value1 = False

        if self.n_display_value is not constants.NUMBER_VALUE_NONE and self.n_value1 is constants.NUMBER_VALUE_NONE:
            self.n_value1 = self.n_display_value
            self.n_display_value = constants.NUMBER_VALUE_NONE

        self.s_operation = self.sender().text()

    # Preform the operation, based on the action button
    def preform_operation(self, n_value1, n_value2, s_operation):
        if self.b_result_is_value1:
            return

        n_result = 0

        if s_operation == constants.OPERATION_BUTTON_ADDITION_STRING:
            n_result = n_value1 + n_value2
        elif s_operation == constants.OPERATION_BUTTON_SUBTRACTION_STRING:
            n_result = n_value1 - n_value2
        elif s_operation == constants.OPERATION_BUTTON_MULTIPLICATION_STRING:
            n_result = n_value1 * n_value2
        elif s_operation == constants.OPERATION_BUTTON_DIVISON_STRING:
            n_result = n_value1 / n_value2

        self.n_display_value = n_result
        self.print_value()

        self.b_result_is_value1 = True
        self.n_value1 = constants.NUMBER_VALUE_NONE
        self.n_value2 = constants.NUMBER_VALUE_NONE
        self.s_operation = constants.NO_OPERATION_VALUE

    # Inverse the display value
    def inverse_display_value(self):
        if self.b_result_is_value1:
            return

        n_temp_value = self.n_display_value
        b_set_value2 = False

        if self.n_value2 == n_temp_value:
            b_set_value2 = True

        self.n_display_value *= -1.0

        if b_set_value2:
            self.n_value2 = self.n_display_value

        self.print_value()

    # Clear the display screen and reset the result private values to None.
    def clear(self):
        self.b_result_is_value1 = False
        self.n_display_value = constants.NUMBER_VALUE_NONE
        self.n_value1 = constants.NUMBER_VALUE_NONE
        self.n_value2 = constants.NUMBER_VALUE_NONE
        self.ui.displayScreen.setText("")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())
