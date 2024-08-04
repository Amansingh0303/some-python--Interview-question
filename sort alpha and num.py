
#sort tha alpha and numbers this format 
# input AXSF1837
# Output Afsx1378


str1 = input("Enter a string in the format(ASD3174):" )
alpha=[]
numbers=[]
for char in str1:
    if char.isalpha():
        alpha.append(char)
    else:
        numbers.append(char)

# print(alpha)

finalist=sorted(alpha)+sorted(numbers)
output= "".join(finalist)
print(output)