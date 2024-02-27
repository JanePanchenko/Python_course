from Python_course.home_task_8.sub_task_1.insufficient_funds_error import InsufficientFundsError


class BankAccount:

    __bank_name = 'Erste'

    def __init__(self, full_name: str, card_number: str, cvv: str, expiration_date: str, balance: float):
        self._full_name = full_name
        self._card_number = card_number
        self.__cvv = cvv
        self.__expiration_date = expiration_date
        self.__balance = balance

    def deposit(self, value: float) -> None:
        updated_balance = self.__balance + value
        self.__balance = updated_balance

    def withdraw(self, value: float) -> None:
        if value < self.__balance:
            updated_balance = self.__balance - value
            self.__balance = updated_balance
        else:
            raise InsufficientFundsError('You don\'t have enough money on your balance')

    @classmethod
    def show_bank_name(cls) -> None:
        print(f'Bank is: {cls.__bank_name}')

    @staticmethod
    def calculate_tax(balance: float, tax_rate: float) -> float:
        return balance * tax_rate

    def get_balance(self) -> float:
        return self.__balance

    def get_full_name(self) -> str:
        return self._full_name

    def set_full_name(self, full_name: str) -> None:
        self._full_name = full_name





