def words(str):
  Words=str.split(" ")
  for i in Words:
    print(i,"-",len(i))
sen=input("Please enter your Sentence")
Words(sen)
print()
