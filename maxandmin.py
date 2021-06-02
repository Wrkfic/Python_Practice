#how to find maximum in the list
def maximum(list):
    max=0
    for i in list:
        if i>max:
            max=i
    return max
list=[]
n=int(input("Please enter len of list:"))
j=0
while j<n:
  ele=int(input("please enter element:"))
  list.append(ele)
  j+=1
print("maximum in the list:%d" %maximum(list))


#how to find minimum in the list
def minimum(list):
    min=0
    for i in list:
        if i<min:
            min=i
    return min
list=[]
n=int(input("Please enter len of list:"))
j=0
while j<n:
  ele=int(input("please enter element:"))
  list.append(ele)
  j+=1
print("minimum in the list:%d" %minimum(list))
