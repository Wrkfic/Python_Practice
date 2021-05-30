def DecimaltoBinary(n):
    value=""
    while n>1:
        a=n%2
        value=str(a)+value
        n=n//2
    value=str(n)+value
    return (value)
dec=int(input("please enter your decimal number:"))
print(DecimaltoBinary(dec))
