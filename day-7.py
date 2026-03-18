
#dictionary

#it is defining with curly braces

student={"name":'teja','age':'21','course':'computer science'}
print(student)
print(student['name'])
print(student['age'])
print(student['course'])
type(student)
print(student.get('age'))
print(student.get('name'))
student['name']='mahanvitha'
student['school']='vvasay'
student['class']='two grade'
student.pop('age')
del student['course']
student.values()

student.update({'city':'hyderabad'})
student.update({'age':'21'})
student.setdefault('city','atchampeta')
student.setdefault('city','atchampeta')
student.pop('age')
student.popitem()

students={
    'anil':{'age':'21','couse':'cs'},
    'bob':{'age':'22','couse':'da'}
    }
print(students['anil']['couse'])

squares={x:x*x for x in range(1,6)}
print(squares)

#finding topper in class
students={
    'kumar':'67',
    'rakesh':'89',
    'suman':'79'
    }
top_student=max(students, key=students.get)
print(top_student)

sentence="hello world hello python"
word_count={}
for word in sentence.split():
    word_count[word]=word_count.get(word, 0)+1
print(word_count)    

#counting words in string
semtence="python is good and python is powerful"
word_count={}
for word in sentence.split():
    word_count[word]=word_count.get(word, 0)+1

   
print(word_count)    

#simple login system
users={
    "admin":"1234",
    "teja":"pass",
    }
username=input("enter username:")
password=input("enter password:")
if users.get(username)==password:
    print("login successful:")
else:
    print("Invalid credentials:")


accounts={
    "teja":{'pin':"1234","balance":5000},
    'kumar':{'pin':'5678','balance':3000}
    }
def login():
    username=input("Enter Username:")
    pin=input("Enter Pin:")
    
    if username in accounts and accounts[username]["pin"] == pin:
        print("Login successful:")
        return username
    else:
        print("Invalid Username:")
        return none
def check_balance(user):
    print(f"balance:{accounts[user]['balance']}")

def deposit(user):
    amount=float(input("Enter amount to deposit:"))
    accounts[user]['balance']+= amount
    print("amount deposited successfully")
def withdraw(user):
    amount= float(input("Enter amount to withdraw"))

    if amount > accounts[user]["balance"]:
        print("Insufficient balance")
    else:
        accounts[user]["balance"] -=amount
        print("Withdrawal successful")

def atm_menu(user):
    while True:
        print("\n======ATM MENU======")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice= input("Enter choice:")

        if choice=="1":
            check_balance(user)
        elif choice=="2":
            deposit(user)
        elif choice=="3":
            withdraw(user)
        elif choice=="4":
            print("Thank you for using ATM")
            break
        else:
            print("Invalid choice")

def main():
    user=login()
    if user:
        atm_menu(user)

main()        
            
                      
                                                   
