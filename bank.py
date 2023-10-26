from history import*

class Bank:
    def __init__(self, name, balance) -> None:
        self.name = name
        self.__current_balance = balance
        self.is_loan = True
        self.__loan = 0
        self.user_account_num = 101
        self.history = []
        self.email_pass = {}
        self.users_with_account_num = {}
        self.admins = {}
        self.loan_feature = True
        self.manager = None
        self.manager_email = None
        self.manager_pass = None

    def add_user(self, user, email, password):
        if email in self.email_pass:
            return 0
        else:
            user.user_email = email
            user.user_pass = password
            user.account_num = self.user_account_num
            self.user_account_num += 1
            self.email_pass[user.user_email] = password
            self.users_with_account_num[user.account_num] = user
            return 1
        
    def user_login(self, email, password):
        if email not in self.email_pass:
            return 0
        if self.email_pass[email] != password:
            return 0
        return 1

    
    def user_diposite(self, user, amount):
        if amount > 0:
            self.__current_balance += amount
            user.user_bal += amount
            dipo = Diposite_his(user, amount)
            self.history.append(dipo)
            user.user_history.append(dipo)
            print(dipo)
        else:
            print('\nNot Enough Money To Diposite.Take More') 
            return

    def user_withdrawal(self, user, amount):
        if self.user_login(user.user_email, user.user_pass) == 1:
            if self.__current_balance == 0 and user.user_bal > 0:
                print('Bank Is Bankrupt')
                return

            if self.__current_balance >= amount > 0:
                self.__current_balance -= amount
                user.user_bal -= amount
                withdrawal = Withdrawal_his(user, amount)
                self.history.append(withdrawal)
                user.user_history.append(withdrawal)
                print(withdrawal)
            else:
                print('\nThis Amount Is Not Valid')
        else:
            print('User not valid')

    def transfer(self, user, reciver_acc_num, amount):
        if self.user_login(user.user_email, user.user_pass) == 1:
            if self.__current_balance == 0 and user.user_bal > 0:
                print('Bank Is Bankrupt')
                return
            
            if reciver_acc_num not in self.users_with_account_num:
                print('This user not available')
                return
            recevier = self.users_with_account_num[reciver_acc_num]

            if self.__current_balance >= amount > 0:
                user.user_bal -= amount
                recevier.user_bal += amount
                send = Transfer_his(user, recevier, amount)
                rece = Receive_his(user, recevier, amount)
                user.user_history.append(send)
                recevier.user_history.append(rece)
                self.history.append(send)
                self.history.append(rece)
                print(send)
                print()
                print(rece)

            else:
                print('\nThis Amount Is Not Valid') 
        else:
            print('User not valid')

    def take_loan(self, user, amount):
        if self.user_login(user.user_email, user.user_pass) == 1:
            if self.is_loan == False:
                print('Your Cannot Take Loan Due To Internal Problem')
                return
            if self.__current_balance == 0 and user.user_bal > 0:
                print('Bank Is Bankrupt')
                return

            if self.__current_balance >= amount > 0:
                self.__current_balance -= amount
                user.user_bal += amount
                user.user_loan += amount
                self.__loan += amount
                loan = Loan_his(user, amount)
                self.history.append(loan)
                user.user_history.append(loan)
                print(loan)
            else:
                print('\nThis Amount Is Not Valid') 
        else:
            print('User Not Valid')


    def add_manager(self, manager, email, password):
        if self.manager == None:
            self.manager_email = email
            self.manager_pass = password
            manager.email = email
            manager.password = password
            self.manager = manager
            return 1
        else:
            return 0
        
    def manager_login(self, email, password):
        if self.manager_email == email and self.manager_pass == password:
            return 1
        else:
            return 0
        
    @property
    def totall_balance(self):
        return self.__current_balance
    
    @property
    def loan_check(self):
        return self.__loan
    
    def loan_function(self, is_on = True):
        self.is_loan = is_on

    def check_transaction_history(self):
        print('######## ALL TRANSACTION HISTORY ########\n')
        for elm in self.history:
            print(elm)






