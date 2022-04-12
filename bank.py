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
    else: return 'Your new balance is ${} after depositing ${}.'.format(self.balance, deposit_amount)

  def withdraw(self, withdrawal_amount):
    self.balance = self.balance - withdrawal_amount
    if (withdrawal_amount < 0):
      return False
    else: return 'Your new balance is ${} after withdrawing ${}.'.format(self.balance, withdrawal_amount)

  def accumulate_interest(self):
    self.balance = (self.balance * self.interest_rate) + self.balance

class ChildrensAccount:
  pass

class OverdraftAccount:
  pass

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
