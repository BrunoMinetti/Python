Str = str(input('entre com uma palavra ')) # initial string
reversedString=[]
index = len(Str) # calculate length of string and save in index
while index > 0: 
    reversedString += Str[ index - 1 ] # save the value of str[index-1] in reverseString
    index = index - 1 # decrement index

corrido=str(reversedString)
print(f'{corrido}') # reversed string
