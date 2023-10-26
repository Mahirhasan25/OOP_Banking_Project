from datetime import datetime
class History:
    def __init__(self, user, amount) -> None:
        self.user_name = user.name
        self.account_num = user.account_num
        self.amount = amount
        self.curr_balance = user.user_bal
        self.time = datetime.today()

class Diposite_his(History):
    def __init__(self, user, amount) -> None:
        super().__init__(user, amount)
    def __repr__(self) -> str:
        return f'''
                    DIPOSITE
        ----------------------------------
        User Name      : {self.user_name}
        Account Number : {self.account_num}
        Diposite       : {self.amount}
        Current Balance: {self.curr_balance}
        Time           : {self.time}
                '''
    
class Withdrawal_his(History):
    def __init__(self, user, amount) -> None:
        super().__init__(user, amount)
    def __repr__(self) -> str:
        return f'''
                    WITHDRAWAL
        ----------------------------------
        User Name      : {self.user_name}
        Account Number : {self.account_num}
        Withdrawal     : {self.amount}
        Current Balance: {self.curr_balance}
        Time           : {self.time}
                  '''
    
class Transfer_his(History):
    def __init__(self, user, receiver, amount) -> None:
        super().__init__(user, amount)
        self.receiver_name = receiver.name
        self.receiver_acc_num = receiver.account_num
    def __repr__(self) -> str:
        return f'''
                    SENDING INFO
        ----------------------------------
        Receiver Name          : {self.receiver_name}
        Receiver Account Number: {self.receiver_acc_num}
        Send Money             : {self.amount}
        Your Current Balance   : {self.curr_balance}
        Time                   : {self.time}
                  '''

class Receive_his(History):

    def __init__(self, user, receiver, amount) -> None:
        super().__init__(user, amount)
        self.receiver_curr_bal = receiver.user_bal

    def __repr__(self) -> str:
        return f'''
                    RECEIVE INFO
        ----------------------------------
        Sender Name          : {self.user_name}
        Sender Account Number: {self.account_num}
        Received Money       : {self.amount}
        Your Current Balance : {self.receiver_curr_bal}
        Time                 : {self.time}
                '''

class Loan_his(History):
    def __init__(self, user, amount) -> None:
        super().__init__(user, amount)
        self.User_loan_money = user.user_loan

    def __repr__(self) -> str:
        return f'''
                    LOAN INFO
        ----------------------------------
        Sender Name          : {self.user_name}
        Sender Account Number: {self.account_num}
        Loan Money           : {self.User_loan_money}
        Your Current Balance : {self.curr_balance}
        Time                 : {self.time}
                '''