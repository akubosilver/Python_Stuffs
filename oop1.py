## Introduction to classes
#first
class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distance(self):
        x = (self.coor1[0] - self.coor2[0])**2
        y = (self.coor1[1] - self.coor2[1])**2
        d = (x + y)**0.5
        print(d)
    def slope(self):
        s = (self.coor1[1] - self.coor2[1])/(self.coor1[0] - self.coor2[0])
        print(s)

class Cylinder():
    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
    def volume(self):
        v = Cylinder.pi * (self.radius**2) * self.height
        print(v)
    def surface_area(self):
        sa = 2 * Cylinder.pi * self.radius * (self.radius + self.height)
        print(sa)
### Challenge Project
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,d_amt):
        self.balance += d_amt
        print("Some amount has been added")
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print("Amount has been withdrawn")
        else:
            print("Not enough fund")
    def __str__(self):
        return f'Acount Owner: {self.owner}\nAcount Balance: {self.balance}'
        

acct1 = Account('Jose', 500)
acct1.withdraw(50)
print(acct1.balance)