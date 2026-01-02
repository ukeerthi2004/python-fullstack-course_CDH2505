#otp three times limit
cotp =  int(input())
att=0
max=3
while att < max:
    eotp=int(input())
    if cotp == eotp:
        print("verified")
    else:
        print("not verifid try")
        att+=1
else:
    print("try agin reset for new code")