# if syntexs
'''
if cond:
    #stmts
if else
----------
if cond:
    #stmts
else:
    #stmts
if-elif-else
-------------
if cond:
    #
elif cond:
    #
elif cond:
    #
    .
    .
    .
    .
----------
#nested if 
if:
    if:
        if:
        else:
    elif:
    elif:
'''
# example 1:
'''cf={'rina','liki','juna','kaina'}
user='rina'
if user in cf:
    print("you can see the story")
f={'rina','liki','juna','kaina'}
ps='public'
user='liki'
if user in f or ps=='public':
    print("view posts")'''

data={
    'lohit': 'li@34',
    'jikjkl': 'jh@657',
    'jhgfxxhjk': 'oi@1234',
    'oiusdfghjk': 't@34567'}
us,pwd= input("enter the username:").split()
if data.get(us)==pwd:
    print(f'hello {us}\n Your login successful!!!')
else:
    print("Invalid login.\nTry again!!!")
        
