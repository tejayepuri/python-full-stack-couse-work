'''
products=['rice','sugar','wheat','flour','milk','eggs','cooking oil','tea powder','salt','soap']
prices=['70','30','45','50','80','40','90','100','30','50']

print("-------here are the grocery store-------")
print("here are available products:\n")
print('Index'.ljust(6,' '),'products'.ljust(10,' '),'prices'.ljust(6,' '))
for i in range(10):
    print(str(i+1).ljust(6,' '),products[i].ljust(10,' '),str(prices[i]).ljust(6,' '))


items=list(map(int,input("enter the inedxes: ").split()))
print('selected item:')
total_amount=0
for item in items:
    print(products[item-1],prices[item-1])
    total_amount+= prices[item-1]
'''




'''
def wish(name):
    print(f'Hello {name}, welcome to "python 100 days of program"')


wish('teja')
wish('anil')
wish('kumar')
name="teja"
wish(name)
'''




'''
def display(username,email,password):
    print("username:",username)
    print("email:", email)
    print("password:",password)

display("teja","teja@gmail.com","teja@123")
display('anil','anil@gmail.com','s@1567')
display('kumar','kumar@gmail.com','w@382749')
'''


'''
def display(username,email,password,phoneno='+91'):
    print("username:",username)
    print("email:", email)
    print("password:",password)
    print("phoneno:",phoneno)

display(username="teja",email="teja@gmail.com",password="teja@123",phoneno='98379349387')
display(username='anil',email='anil@gmail.com',password='s@1567',phoneno='9389473894')
display(username='kumar',email='kumar@gmail.com',password='w@382749',phoneno='0937794839')
'''



'''
def display(*names):
    print(names)

display("tharun","gowtham","akhil")
display("tharun","gowtham")
display("tharun")
'''
