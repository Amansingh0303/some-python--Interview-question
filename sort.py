# li=[22,31,12,13,10,9,5,6] 
# sar_no= sorted(li)
# print(sar_no)

#find the maximum value without max function

li=[22,31,12,131,10,9,5,6,1]      
li.sort()
print("max no in list",li[-1])
print("min no of list ",li[0])

# numberli=[22,31,12,13,10,9,5,6]
# maxnuber=numberli[0]
# for num in numberli:
#     if maxnuber < num:
#         maxnuber = num
# print(maxnuber) 

# find the minmun value of list 

# numberli=[22,31,12,13,10,9,5,6]
# maxnuber=numberli[0]
# for num in numberli:
#     if maxnuber > num:
#         maxnuber = num
# print(maxnuber) 


# count the white space

# str = "P  r gramin g"
# print(str.count(" "))


# Find the no of  middle list 

# numlist = [9,5,7,4,8,6]
# midelement= int(len(numlist)/2)
# print(numlist[midelement])

# descending And revese value without inbuild function
 
# ste=[" PYTHON PROGRAMMING "]
# # li.sort()
# print=(ste[::-1])





# Adding two no using list comprehension

lis1 = [21 , 7 , 17 ,4]
lis2 = [11 , 9 , 7 ,5]

result = [lis1[i]+lis2[i] for i in range(len(lis1))]
print(result)

# Adding two no using loop 

# lis1 = [2 , 7 , 7 ]
# lis2 = [11 , 9 , 8 ]
# adda = []
# for i in range(len(lis2)):
#     adda.append(lis1[i]+lis2[i])
# print(adda)

 # Converting list into string

lst = ['P', 'Y','T','H','O','N']
string= ''.join(lst)
# print(type(string))
print(type(lst))

# reverse  string using slicing 

original = (" PYTHON ")
reverse= original[::-1]
print(reverse)





#  Python program to find the odd numbers in an array

# numbers = [8,3,1,6,2,4,5,9]
# count = 0
# for i in range(len(numbers)):
#     if(numbers[i]%2!=0):    
#         count = count+1
# print("The number of odd numbers in the list are: ", count)


# number=int(input("Enter a number to Check: "))

# if number%2==0:
#     print("Number is even",number)
# else:
#     print("Number is odd",number)


# fine the even no

# numbers = [8,2,2,6,2,4,5,9]
# count = 0
# for i in range(len(numbers)):
#     if(numbers[i]%2==0):
#         count = count+1
# print("The number of even numbers in the list are: ", count)







# class am:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# class am1(am):
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id
# s1=am('sudeep',30)
# s2=am1('shubham',20,1)
# print(s1.name )


 




