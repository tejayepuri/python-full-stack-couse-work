'''class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._posts=[]

    def myposts(self):
        return self._posts
    def myposts(self,postname):
        self._posts.append(postname)

    def get_password(self):
        return self_password
    def set_password(self,new_password):
        self._password=new_password'''



'''class Instagram:
    def reel(self):
        print("you can post the reel")

teja=Instagram()
teja.reel()'''

'''class InstagramV1:
    def reel(self):
        print("you can post the reel")

print('teja  ----   Instagram')
teja=InstagramV1()
teja.reel()'''


'''class InstagramV1:
    def reel(self):
        print("you can post the reel")

class InstagramV2(InstagramV1): #inheritance
    def story(self):
        print("you can upload a story")

print('teja  ----   InstagramV1')        
teja=InstagramV1()
teja.reel()

print('anil  ----   InstagramV2')        
anil=InstagramV2()
anil.reel()
anil.story()'''

class Vehicle: 
    def __init__(self, brand): 
        self.brand = brand 
    def start(self): 
        print(f"{self.brand} vehicle started.") 
 
class Car(Vehicle): 
    def __init__(self, brand, model): 
        super().__init__(brand) 
        self.model = model 
    def show_info(self): 
        print(f"Brand: {self.brand}, Model: {self.model}")
        
car1 = Car("Toyota", "Camry") 
car1.start() 
car1.show_info()



class Account:
    def __init__(self,balance):
        self.balance=balance
    def show_balance(self):
        print(f"balance: {self.balance}")
class savingsAccount(Account):
    def __init__(self,balnce,interest_rate):
        super().
