def check_amstrong(n):
    value=0
    for i in str(n):
        a=int(i)**len(str(n))
        value+=a
    if value==n:
        print("Amstrong Number")
    else:
        print("Not a Amstrong Number")
num=int(input("Please enter your number:"))
check_amstrong(num)
