
from bank import Bank
from client import User
from manager import Manager

def main():
    bank = Bank('sonali bank', 100000)
    user1 = User('Abir', 977655)
    user1.create_account(bank)
    # user2 = User('sakib', 1298)
    # user2.create_account(bank)

    # user1.diposite(7000, bank)
    # user1.send_money(2000, 102, bank)
    
    user1.login_account(bank)

    # user1.diposite(50000, bank)

    # user1.Withdrawal(2000, bank)
    # manager1 = Manager('Shakil')
    # # manager2 = Manager('pasha')
    # manager1.create_account(bank)
    # # manager1.check_avaiable_balance_of_bank(bank)
    # # manager1.check_loan_of_bank(bank)
    # manager1.login_account(bank)
    # manager2.create_account(bank)
    # print(bank.is_loan)
    # manager1.loan_feature(bank, False)
    # print(bank.is_loan)








if __name__ == '__main__':
    main()