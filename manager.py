
def bool_input():
    user_input = input('\nEnter True or False: ')
    if user_input == "True":
        return True
    elif user_input == "False":
        return False
    else:
        raise ValueError("Invalid boolean input")
    

class Manager:
    def __init__(self, name) -> None:
        self.name = name
        self.email = None
        self.password = None

    def create_account(self, bank):
        print('\n<< Create Manager Account >>')
        email = input('\nEnter your email: ')
        password = input('Enter your password: ')
        flag = bank.add_manager(self, email, password)
        if flag == 1:
            print('\nManager Account Is Completed')
        else:
            print('\nManager Account Exist.Please login..')
    
    def login_account(self, bank):
        print('\n<< Login Manager Info >>')
        email = input('\nEnter your email: ')
        password = input('Enter your password: ')
        flag = bank.manager_login(email, password)
        if flag == 0:
            print('\nUser Not Found.Please Check Your Email and password')
            return
        else:
            print('\nLogin Succesfull')

            while True:
                print('\nPress 1 to check ballance')
                print('Press 2 to check loan')
                print('Press 3 to loan feauture on or off')
                print('Press 4 to check transanction history of bank')
                print('Press any to exit')
                key = int(input('\nInput: '))

                if key == 1:
                    self.check_avaiable_balance_of_bank(bank)
                elif key == 2:
                    self.check_loan_of_bank(bank)
                elif key == 3:
                    swich = bool_input()
                    print(swich)
                    self.loan_feature(bank, swich)
                elif key == 4:
                    self.see_history_of_bank(bank)
                else:
                    print('Program Closed')
                    break

    def check_avaiable_balance_of_bank(self, bank):
        print('\nCurrent Balance of Bank:',bank.totall_balance)

    def check_loan_of_bank(self, bank):
        print('\nTotall Loan fo Bank: ', bank.loan_check)

    def loan_feature(self, bank, swich_on = True):
        bank.loan_function(swich_on)
    
    def see_history_of_bank(self, bank):
        bank.check_transaction_history()
        
            
    