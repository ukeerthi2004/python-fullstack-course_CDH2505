#for loop
"""
for var in seq:
    #stmts
seq : list,tuple,set,dict,str,range
"""
"""products = {
    "qwer":3445,
    "djjf":5637,
    "jduks":3484,
    "fjjd":2344,
}
for i in products:
    print(f'{i}: ${products[i]}')
    print(i,products[i])
"""
'''s='Python Programming'
vol='aeiouAEIOU'
for i in s:
    if i in vol:
        print(f'{i}--v')
    else:
        print(f'{i}**C')
'''
#range(start,stop+1,step)
'''table = int(input("Enter the table"))
for i in range(1,21):
    print(f'{table}*{i}={table*i}')

table = int(input("Enter the table"))
for i in range(10,0,-1):
    print(f'{table}*{i}={table*i}')
'''
'''l=['hgfgh','jhgfdfg','hgfdfgh','reert']
for i in range(len(l)):
    print(i,l[i])'''

l=('hgfgh','jhgfdfg','hgfdfgh','reert')
for i in enumerate(l):
    print(i,)
