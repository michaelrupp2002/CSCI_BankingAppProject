from PyQt5.QtWidgets import *
from view import *
import csv


class Controller(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        """
        Function to set up buttons and accounts
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.__account_balance = 0
        self.button_deposit.clicked.connect(lambda: self.deposit(self.input_amount.toPlainText()))
        self.button_withdraw.clicked.connect(lambda: self.withdraw(self.input_amount.toPlainText()))
        self.button_select.clicked.connect(lambda: self.select())

        with open('accounts.csv', 'w', newline='') as self.__account_file:
            thewriter = csv.writer(self.__account_file)
            thewriter.writerow([self.comboBox_account.itemText(0), self.comboBox_account.itemData(0)])
            thewriter.writerow([self.comboBox_account.itemText(1), self.comboBox_account.itemData(1)])
            thewriter.writerow([self.comboBox_account.itemText(2), self.comboBox_account.itemData(2)])

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
                self.label_errors.setText('$' + str(amount) + ' has been deposited.')
                self.overwrite()
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
                self.label_errors.setText('$' + str(amount) + ' has been withdrawn.')
                self.overwrite()
            else:
                if float(amount) > self.__account_balance:
                    self.label_errors.setText('Insufficient funds, please try a smaller amount.')
                else:
                    self.label_errors.setText('Could not withdraw, please enter a positive amount.')
        except ValueError:
            self.label_errors.setText('Please enter an amount of money.')

    def select(self):
        """
        Function to set current balance to correct amount upon clicking select button.
        :return:
        """
        self.__account_balance = self.comboBox_account.currentData()
        self.label_currentBalance.setText('Current Balance: $' + str(self.comboBox_account.currentData()))

    def overwrite(self):
        """
        Function to overwrite data on the csv file for the three pre-made accounts.
        :return:
        """
        with open('accounts.csv', 'w', newline='') as self.__account_file:
            thewriter = csv.writer(self.__account_file)
            if self.comboBox_account.currentText() == 'Account 5439':
                self.comboBox_account.setItemData(0, self.__account_balance)
                thewriter.writerow([self.comboBox_account.itemText(0), self.__account_balance])
                thewriter.writerow([self.comboBox_account.itemText(1), self.comboBox_account.itemData(1)])
                thewriter.writerow([self.comboBox_account.itemText(2), self.comboBox_account.itemData(2)])
            elif self.comboBox_account.currentText() == 'Account 1055':
                self.comboBox_account.setItemData(1, self.__account_balance)
                thewriter.writerow([self.comboBox_account.itemText(0), self.comboBox_account.itemData(0)])
                thewriter.writerow([self.comboBox_account.itemText(1), self.__account_balance])
                thewriter.writerow([self.comboBox_account.itemText(2), self.comboBox_account.itemData(2)])
            else:
                self.comboBox_account.setItemData(2, self.__account_balance)
                thewriter.writerow([self.comboBox_account.itemText(0), self.comboBox_account.itemData(0)])
                thewriter.writerow([self.comboBox_account.itemText(1), self.comboBox_account.itemData(2)])
                thewriter.writerow([self.comboBox_account.itemText(2), self.__account_balance])
