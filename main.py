
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
    

    #fist comment







if __name__ == '__main__':
    main()