class bankaccount:
    def __init__(self,
account_number,
account_holder_name,
initial_balance=0):
        self.__account_number=account_number
self.__account_holder_name=account_holder_name
              self.__account_balance= initial_balance

    def deposit(self,amount):
        if amount > 0 :

self.__account_balance +=amount
            return true
      else:
            return false  #
cannot deposit a non-positive amount

    def withdraw(self,amount):
        if 0 < amount <=
self.__account_balancee:

self.__account_balance -=amount
            return true
        else:
            return false  #
withdrawal amount exceeds
balance or is non-positive

    def display_balance(self):
        return f"account
holder:
{self.__account_holder_name},
account number:
{self.__account_number},
balance: $
{self.__account_balance:.2f}"

# example usage:
if __name__ == "__main__":
    # create an instance of bankaccount
    my_account =
bankaccount("123456789","john doe", 1000)

    #deposit $500
    if
my_account.deposite(500):
        print("deposited $500 successfully.")
    else:
        print("invalid depositamount.")

    # withdraw $200
    if
my_account.withdraw(200):
        print("withdrawn $200 successfully.")
    else:
        print("invalid withdrawal amount or insufficien balance.")

      # display account balance

print(my_account.display_balance())
