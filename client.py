
class User:
    def __init__(self, name, nid_card) -> None:
        self.name = name
        self.__nid_card = nid_card
        self.account_num = None
        self.user_email = None
        self.user_pass = None
        self.user_bal = 0
        self.user_loan = 0
        self.user_history = []

    def create_account(self, bank):
        print('\n-- Create User Account --')
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        flag = bank.add_user(self, email, password)
        if flag == 1:
            print('\nAccount Is Completed')
        else:
            print('\nThis Email Is Already Exist.Please Try Another')
    
    def login_account(self, bank):
        print('\n-- Login User Info --')
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        flag = bank.user_login(email, password)
        if flag == 0:
            print('\nUser Not Found.Please Check Your Email and password')
            return
        else:
            print('\nLogin Succesfull')
        
            while True:
                print('\nPress 1 to check ballance')
                print('Press 2 to diposit')
                print('Press 3 to withdraw')
                print('Press 4 to send money')
                print('Press 5 to loan')
                print('Press 6 history')
                print('Press any to exit')

                key = int(input('\nInput: '))
                if key == 1:
                    self.check_balance()
                elif key == 2:
                    amount = int(input('Enter amount: '))
                    self.diposite(amount, bank)
                elif key == 3:
                    amount = int(input('Enter amount: '))
                    self.Withdrawal(amount, bank)
                elif key == 4:
                    amount = int(input('Enter amount: '))
                    acc_num = int(input('Reciver Account Number: '))
                    self.send_money(amount, acc_num, bank)
                elif key == 5:
                    amount = int(input('Enter amount: '))
                    self.request_for_loan(amount, bank)
                else:
                    print('Program Closed.')
                    break

    def check_balance(self):
        print('\nCurrent Balance: ', self.user_bal)

    def diposite(self, amount, bank):
        bank.user_diposite(self, amount)

    def Withdrawal(self, amount, bank):
        if self.user_bal >= amount > 0:
            bank.user_withdrawal(self, amount)
        else:
            print('Your Balance Is Insufficient')
    
    def send_money(self, amount, reciver_account_number, bank):
        if self.user_bal >= amount > 0:
            bank.transfer(self, reciver_account_number, amount)
        else:
            print('Your Balance Is Insufficient')
    
    def request_for_loan(self, amount, bank):
        if 0 < amount <= self.user_bal * 2:
            bank.take_loan(self, amount)
        else:
            print('This Amount Is Too Much or Too Short to Take Loan.')
    
    def user_history(self):
        print('######## USER HISTORY ########\n')
        for elm in self.user_history:
            print(elm)
        
