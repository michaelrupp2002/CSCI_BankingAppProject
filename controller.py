from PyQt5.QtWidgets import *
from view import *


class Controller(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        """
        Function to set up buttons
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.__account_balance = 0
        self.button_deposit.clicked.connect(lambda: self.deposit(self.input_amount.toPlainText()))
        self.button_withdraw.clicked.connect(lambda: self.withdraw(self.input_amount.toPlainText()))

    def deposit(self, amount: float):
        """
        Function to deposit amount from input
        :param amount: Amount of money to add as a float or int
        :return: None
        """
        try:
            if float(amount) > 0:
                self.__account_balance += float(amount)
                self.input_amount.clear()
                self.label_currentBalance.setText('Current Balance: $' + str(self.__account_balance))
                self.label_errors.setText('Your money has been deposited.')
            else:
                self.label_errors.setText('Could not deposit, please enter a positive amount.')
        except ValueError:
            self.label_errors.setText('Please enter an amount of money.')

    def withdraw(self, amount: float):
        """
        Function to deposit amount from input
        :param amount: Amount of money to add as a float or int
        :return: None
        """
        try:
            if 0 < float(amount) <= self.__account_balance:
                self.__account_balance -= float(amount)
                self.input_amount.clear()
                self.label_currentBalance.setText('Current Balance: $' + str(self.__account_balance))
                self.label_errors.setText('Your money has been withdrawn.')
            else:
                if float(amount) > self.__account_balance:
                    self.label_errors.setText('Insufficient funds, please try a smaller amount.')
                else:
                    self.label_errors.setText('Could not withdraw, please enter a positive amount.')
        except ValueError:
            self.label_errors.setText('Please enter an amount of money.')
