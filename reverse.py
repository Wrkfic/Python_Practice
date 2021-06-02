#first method to reverse word
def reverse_string_m1(str):
  result=str[::-1]
  return result
str=input("please enter your word:")
print(reverse_string_m1(str))

#second method to reverse word
def reverse_word_m2(str):
  result=""
  for i in str:
    result=i+result
  return result
str=input("please enter your word:")
print(reverse_word_m2(str))


#first method to resversing the number
def reverse_num_m1(n):
    if n<0:
        value=str(n)
        print("-%s" %value[:0:-1])
    else:
        value=str(n)
        print(value[::-1])
num=int(input("Please enter your number:"))
reverse_num_m1(num)

#second method to reverse the number
def reverse_num_m2(n):
    num=abs(n)
    reverse=0
    while num>0:
        rem=num%10
        reverse=reverse*10 + rem
        num=num//10
    if n>0:
        print(reverse)
    else:
        print(reverse*-1)
number=int(input("Enter your number:"))
reverse_num_m2(number)
  
