"""
class Myclass:
    i=1234
    def f(self):
        print("haello ")

obj=Myclass()
obj.f()
"""
class Bankaccount:

  count=1000
  balance=0.0
          
  def setname(self):
      name=input("Enter your name")
      print(name)

  def setgender(self):
      gender=input("Enter your gender")
      print( gender)

  def setact(self):
      typeofac=input("Enter your type")
      print(typeofac)   

  def deposit(self):
     amount=int(input('Enter the amount to deposit:'))
     self.balance+=amount
     print('Your New Balance =%d' %self.balance)

  def withdraw(self):
      amount=int(input('Enter the amount to withdraw:'))
      if(amount>self.balance):
       print('Insufficient Balance!')
      else:
       self.balance-=amount
       print('Your Remaining Balance =%d' %self.balance)  



if __name__ =='__main__':
  obj=Bankaccount()
  #obj.display()
  obj.setname()
  obj.setgender()
  obj.setact()
  obj.deposit()
  obj.withdraw()





























































"""
   def deposit(self):
   amount=int(input('Enter the amount to deposit:'))
   self.balance+=amount
   print('Your New Balance =%d' %self.balance)

   def withdraw(self):
   amount=int(input('Enter the amount to withdraw:'))
if(amount>self.balance):
print('Insufficient Balance!')
else:
self.balance-=amount
print('Your Remaining Balance =%d' %self.balance)
def enquiry(self):
print('Your Balance =%d' %self.balance)
account= Account()
account.deposit()
account.withdraw()
account.enquiry()

"""
