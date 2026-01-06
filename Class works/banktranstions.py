data = {
    2344 : {'balance':989000,'transtaionhistory' : []},
    3445 : {'balance':6000,'transtaionhistory' : []},
    4567 : {'balance':489000,'transtaionhistory' : []}
}
def login(pin):
    if pin in data:
        print("login successfull")
        return True
    else:
        print("Invaild pin ")
        return False
    
def checkbalnce(pin):
        print(f"(Balance amount : ₹{data[pin]['balance']})")

def deposit(pin):
    amount = float(input("enter the amount"))
    data[pin]['balance'] += amount
    data[pin]['transtaionhistory'].append(f"₹{amount} is deposited")
    print("Deposite successfull")
def withdraw(pin):
    amount = float(input("Enter the amount"))
    if amount <= data[pin]['balance']:
        data[pin]['balance'] -= amount
        data[pin]['transtaionhistory'].append(f"₹{amount} is withdraw")
        print("Amount is withdraw")
    else:
        print("insufficient balance")
def view_transistions(pin):
    if data[pin]['transtaionhistory']:
        print('history')
        for i in data[pin]['transtaionhistory']:
            print(i)
        else:
            print("end of the transtions")
    else:
        print("No transactions")

u_pin = int(input("pin number: "))

if login(u_pin):
    while True:
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View transitions")
        print("0. Exit")
        ch = int(input("choice:"))
        if ch==1:
            checkbalnce(u_pin)
        elif ch==2:
            deposit(u_pin)
        elif  ch==3:
            withdraw(u_pin)
        elif ch==4:
            view_transistions(u_pin)
        elif ch==0:
            print("Thanks")
            break
        else:
            print('invaild choice')
