
'''
#set

#membership

set={1,2,3,4,5}
print(2 in set)
print(6 in set)


#Union

set1={1,2,3,4}
set2={4,5,6,7}
result=set1|set2

#intersection

set1={1,2,3,4}
set2={4,5,6,7}
result=set1&set2

#difference
set1={1,2,3}
set2={3,4,5}
result=set1-set2

#symmertic difference
set1={1,2,3}
set2={3,4,5}
result=set1^set2


#subset
set1={1,2,3}
set2={3,4,5}
result=set1<=set2

#superset
set1={1,2,3}
set2={3,4,5}
result=set1>=set2

#disjoint sets

set1={1,2,3}
set2={6,4,5}
print(set1.isdisjoint(set2))


list1=[1,2,3,4]
list2=[3,4,5,6]
if set(list1)&set(list2):
    print("common elemments exist")
else:
    print("no common elements")
'''

#project:Unique visitor tracker

visitors = set()

def add_visitor():
    visitor_id = input("Enter Visitor ID: ")
    if visitor_id in visitors:
        print("Visitor already recorded!")
    else:
        visitors.add(visitor_id)
        print("Visitor added successfully!")

def view_visitors():   
    print("\nUnique Visitors List:")
    for v in visitors:
        print(v)
    print(f"Total unique visitors: {len(visitors)}")  

def main():
    while True:
        print("\n----- Unique Visitor Tracker -----")
        print("1. Add Visitor")
        print("2. View Visitors")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_visitor()
        elif choice == "2":
            view_visitors()   
        elif choice == "3":
            print("Exiting....")
            break
        else:
            print("Invalid choice")

main()
