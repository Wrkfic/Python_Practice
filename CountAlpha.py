#code will count alphabets, commas, special character, etc. In other words it removes whitespaces between your given sentebces.
def lettercount(string):
    l=string.split(" ")
    length=0
    for i in l:
        length+=len(i)
    return length
sentence=input("please enter your sentence:")
print(lettercount(sentence))           #this will return the number of alphabates ans characters in your sentence after removing whitespace from it.
