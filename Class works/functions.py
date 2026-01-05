'''data = {
    2344 : {'balance':989000,'transtaionhistory' : []},
    3445 : {'balance':6000,'transtaionhistory' : []},
    4567 : {'balance':489000,'transtaionhistory' : []}
}
def checkbalnce(pin):
    if pin in data:
        print(f"(Balance amount : ${data[pin] ['balance']})")
checkbalnce(3445)
#pass by value
def display(n):
    n[4]=16
    print(f'Inside: {n}')
n = {1:1,2:4,3:9}
display(n)
print(f"outside: {n}")

#pass by reference
def display(n):
    n = n.copy()
    n.append(5)
    print(f'Inside: {n}')
n = [1,2,3,4]
display(n)
print(f"outside: {n}")

def display(n):
    if n==0:
        return
    print(n)
    display(n-1)

display(5)
'''

def pattern(ind):
    if ind ==len(s):
        return
    print(s[:ind+1])
    pattern(ind+1)
s='abcdef'
pattern(0)

def pattern(s,n,ind=0):
    if ind > len(s) -1:
        return
    print(s[ind:ind+n])
    pattern(s,n,ind+1)
s='abcdef'
n=int(input())
pattern(s,n)

def pattern(ind,w):
    if ind == len(s) -w+1:
        return
    print(s[ind:ind+w])
    pattern(w,ind+1)
s='abcdef'
w=int(input())
pattern(s,w)

