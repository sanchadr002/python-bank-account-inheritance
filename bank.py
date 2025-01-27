class BankAccount:
  def __init__(self, balance = 0, interest_rate = .02):
    self.balance = balance
    self.interest_rate = interest_rate

  def __str__(self):
    return 'Current balance is ${}.'.format(self.balance)

  def deposit(self, deposit_amount):
    self.balance = self.balance + deposit_amount
    if (deposit_amount < 0):
      return False
    else: return self.balance

  def withdraw(self, withdrawal_amount):
    self.balance = self.balance - withdrawal_amount
    if (withdrawal_amount < 0):
      return False
    else: return self.balance

  def accumulate_interest(self):
    self.balance = (self.balance * self.interest_rate) + self.balance
    return self.balance

class ChildrensAccount:
  def __init__(self, balance = 0, interest_rate = 0):
    self.balance = balance
    self.interest_rate = interest_rate

  def __str__(self):
    return 'Current balance is ${}.'.format(self.balance)
  
  def deposit(self, deposit_amount):
    self.balance = self.balance + deposit_amount
    if (deposit_amount < 0):
      return False
    else: return self.balance
  
  def withdraw(self, withdrawal_amount):
    self.balance = self.balance - withdrawal_amount
    if (withdrawal_amount < 0):
      return False
    else: return self.balance

  def accumulate_interest(self):
    self.balance = self.balance + 10
    return self.balance

class OverdraftAccount:
  def __init__(self, overdraft_penalty = 40, balance = 0, interest_rate = .02):
    self.balance = balance
    self.overdraft_penalty = overdraft_penalty
    self.interest_rate = interest_rate
  
  def __str__(self):
    return 'Current balance is ${}.'.format(self.balance)

  def deposit(self, deposit_amount):
    self.balance = self.balance + deposit_amount
    if (deposit_amount < 0):
      return False
    else: return self.balance
    
  def withdraw(self, withdrawal_amount):
    self.balance = self.balance - withdrawal_amount
    if (withdrawal_amount < 0 or withdrawal_amount > self.balance):
      self.balance = self.balance - self.overdraft_penalty
      return False
    else: return self.balance

  def accumulate_interest(self):
    if (self.balance < 0):
      self.balance = self.balance
    else: 
      self.balance = (self.balance * self.interest_rate) + self.balance
    return self.balance

basic_account = BankAccount()
print(basic_account)
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
