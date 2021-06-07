# Below code will help to finding the minimum difference between entered number and the numbers in list.
def nearest(list,n):
    near=[]
    for i in list:
        value=n-i
        near.append(abs(value))
    return min(near)
noe=int(input("enter the length of list:"))
list=[]
i=0
while i<noe:
    ele=int(input("enter your element:"))
    list.append(ele)
    i+=1
sn=int(input("enter the number:"))
print("Minimum difference between entered number and number in list :",nearest(list,sn))
