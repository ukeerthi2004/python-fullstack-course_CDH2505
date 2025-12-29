#A nested for loop means
#👉 one for loop inside another for loop.

'''
for outer in sequence1:
    for inner in sequence2:
        statement
'''
#-----examples------

for row in range(5):
    for col in range(5):
        print("*",end =' ')
    print()
'''
* * * * * 
* * * * * 
* * * * *
* * * * *
* * * * *
'''
for row in range(5):
    for col in range(5):
        print(col+1,end =' ')
    print()
'''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''
for row in range(5):
    for col in range(6):
        print(row+1,end =' ')
    print()
'''
1 1 1 1 1 1
2 2 2 2 2 2
3 3 3 3 3 3
4 4 4 4 4 4
5 5 5 5 5 5
'''
for row in range(1,6):
    for col in range(row):
        print("*",end =' ')
    print()
'''
*
* *
* * *
* * * *
* * * * *
'''
for row in range(5,0,-1):
    for col in range(row):
        print("*",end =' ')
    print()

#one more pattern
n=int(input())
for row in range(n):
    for col in range(n-row):
        print("*",end =' ')
    print()
'''
* * * * *
* * * *
* * *
* *
*
'''
n=int(input())
for row in range(n):
    for spc in range(n-1-row):
        print(" ",end=' ')
    for col in range(row+1):
        print("*",end =' ')
    print()
'''
        *
      * *
    * * *
  * * * *
* * * * *
'''
n=int(input())
for row in range(n):
    for spc in range(row):
        print(" ",end=' ')
    for col in range(n-row):
        print("*",end =' ')
    print()
'''
* * * * *
  * * * *
    * * *
      * *
        *
'''
n=int(input())
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()
'''
* * * * * * * * * *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
* * * * * * * * * *
'''
n=int(input())
for row in range(n):
    for col in range(n):
        if row==col  or row+col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()
'''
*       * 
  *   *
    *
  *   *
*       *
'''