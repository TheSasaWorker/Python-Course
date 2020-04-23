

class BankAccount:

# INIT FUNCTION
    def __init__(self, owner, age):

        self.owner = str(owner)
        self.age = int(age)
        self.balance = 250
        self.debt = 1000
        self.interest_rate = 3
        self.full_name = self.owner.split(' ')
        self.first_name = self.full_name[0]
        self.last_name = self.full_name[1]

# FUNCTION TO GET /bal
    def getBalance(self):
        print('Your current balance is: $' + str(self.balance))
        return self.balance

# FUNCTION TO GET DEBT
    def getDebt(self): 
        print('You currently owe in debt to the bank: $' + str(self.debt))
        return self.debt

# - BAL
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print('You have withdrawn $' + str(amount) + ' and now have $' + str(self.balance) + ' left.')
            return self.balance
        else:
            print('You do not have enough balance to perform this operation.')
            return -1

# + BAL
    def deposit(self, amount):
        self.balance += amount
        print('You have deposited $' + str(amount) + ' and now have $' + str(self.balance) + ' in your bank account.')
        return self.balance

# - DEBT
    def debt_pay(self, amount): 
        if amount > self.balance:
            print('You do not have enough balance to perform this operation.')
        elif amount > self.debt:
            self.balance -= amount
            self.debt = 0
            print('You have paid your debt! Thank you for your donation! Your balance is now: $' + str(self.balance) + ' and your debt is now 0$')
        else:
            self.balance -= amount
            self.debt -= amount
            print('You now have $' + str(self.debt) + ' left. Your balance is now $' + str(self.balance))

# INTEREST RATE
    def getinterest_rate(self):
        print('Your interest rate is: %' + str(self.interest_rate))
        return self.interest_rate

# DESTRUCT FUNCTION
    def __del__(self):
        print('You have deleted your account named ' + self.owner)

# BANK, INHERITED BANK ACCOUNT
class Bank(BankAccount):

    def __init__(self, name, address, state, owner):
        self.name = name
        self.address = str(address)
        self.state = state
        self.owner = owner
        self.stored_money = 20000
        self.bank_interest_rate = 3
        self.total_debt = 30000
        self.business_id = 'ROING123123'
        self.phone_number = '0712312312'

#/bal
    def safe_bal(self): 
        print('The safe\'s current balance is: $' + str(self.balance)')
        return self.stored_money

# +bal
    def safe_add(self, amount):
        self.stored_money += amount
        print('You have deposited $' + str(amount) + ' and now have $' + str(self.stored_money) + ' in the safe.')
        return self.stored_money

# BUSINESS CARD
    def business_card(self): 
        print('Name: ' + self.name + '\n' + 'Address: ' + self.address + '\nState: ' + self.state + '\nBusiness ID: ' + self.business_id + '\nPhone Number: ' + self.phone_number)
        return self.business_id

# BANK INTEREST RATE
    def bank_interest_rate(self): 
        print('The bank\'s official interest rate is: %' + str(self.bank_interest_rate))
        return self.bank_interest_rate

# TOTAL DEBT
    def get_total_debt(self): 
        print('There is a total of $' + str(self.total_debt) + ' owed to the bank.')
        return self.total_debt

# take a guess
    def __del__(self):
        print('Bank ROING123123 has been successfully deleted.')
