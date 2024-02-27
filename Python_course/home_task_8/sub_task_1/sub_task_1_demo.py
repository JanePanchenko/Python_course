from Python_course.home_task_8.sub_task_1.bank_account import BankAccount
from Python_course.home_task_8.sub_task_1.insufficient_funds_error import InsufficientFundsError

bank_account = BankAccount('Yevheniia Panchenko', '5000 7000 9000 1111', '579', '10.10.2027', 500.00)
print(f'Your current balance is: {bank_account.get_balance()}')
try:
    print('Withdrawing 330')
    bank_account.withdraw(330.00)
    print(f'Your current balance is: {bank_account.get_balance()}')
    print('Withdrawing 250')
    bank_account.withdraw(250.00)
except InsufficientFundsError as ex:
    print(ex.message)
print(f'Your current balance is: {bank_account.get_balance()}')
bank_account.show_bank_name()
print(f'Tax for your balance is : {BankAccount.calculate_tax(bank_account.get_balance(), 0.05)}')
print(f'Full Name: {bank_account.get_full_name()}')
print('Updating Full Name')
bank_account.set_full_name('Jane Panchenko')
print(f'Full Name: {bank_account.get_full_name()}')
