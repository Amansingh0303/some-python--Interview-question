# list comprehention  Normal syntax - 01
# [expression for variable in iterable]

num = [2,16,8,9,5,4,13,12,6]
# sq=[]
# for i in num :
#     sq.append(i*i)
# print(sq)

print([ i*i for i in num ])


# list comprehention syntax If Condition  - 02
# [expression for variable in iterable in if cond]



# num = [2,16,8,9,5,4,13,12,6]
# sq=[]
# for i in num:
#     if i%2==0:
#         sq.append(i)
# print(sq)

# num = [2,16,8,9,5,4,13,12,6]
# sq=[]
# for i in num:
#     if i%2==0:
#         sq.append(i*i)
# print(sq)

# [expression for variable in iterable in if cond]

# print([i*i for i in num if i%2==0])






# list comprehention syntax  nested If 's  - 03
# [expression for variable in iterable if cond1 if cond2]

# num = [2,16,8,9,5,4,13,12,6]
# sq=[]
# for i in num:
#     if i%2==0:
#         if i%3==0:
#             sq.append(i*i)
        
# print(sq)

# print([i*i for i in num if i%2==0 if i%3==0 ])







# list comprehention syntax  if - Else  - 04 
# [expression if cond else expression for variable in itrable]

num = [2,16,8,9,5,4,27,15,6]
# sq=[]
# for i in num:
#     if i%2==0:
#         sq.append(i*i)
#     else:
#         sq.append(i*i*i)
# print(sq)
print([i*i if i%2==0 else i*i*i for i in num])











