num = int(input("Enter a number: "))
sum = 0
temp = num

t=num
count = 0
while t > 0:
    count += 1
    t = t //10
digits = 0
while temp > 0:
    digits = temp % 10
    sum += (digits ** count)
    temp = temp // 10
else:
    if sum == num:
        print("Amostrong")
    else:
        print("Not amostrong")

