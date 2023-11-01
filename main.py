
from bank import Bank
from client import User
from manager import Manager

def main():
    
    bank = Bank('sonali bank', 100000)
    user1 = User('Abir', 977655)
    manager1 = Manager('Rajim')

    print('Press 1 For User Account')
    print('Press 2 For Manager Account')
    press = int(input('>> '))
    if press == 1:
        user1.create_account(bank)
        user1.login_account(bank)
    elif press == 2:
        manager1.create_account(bank)
        manager1.login_account(bank)
    else:
        print('Keword Unvalid.Please Try again..')






if __name__ == '__main__':
    main()