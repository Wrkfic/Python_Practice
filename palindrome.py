#With help of function to check palindrome 
def palindrome(str): 
  result=""
  if str=str[::-1]:
    result="Palindrome"
  else:
    result="Not Palindrome"
  return result
s=input("please enter your word:\n")
print(palindrome(s))

#without creating funtion:
S=input("Enter your word:\n")
if S==S[::-1]:
  print("Provided word is Palindrome")
else:
  print("Provided word is not a Palindrome")
