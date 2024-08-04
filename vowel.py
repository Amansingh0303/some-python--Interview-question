# counting the vowel

vowel = ['a','e','i','o','u']
# word = 'programming'
word = input(" Enter the word: ")

count=0
for character in word:
    if character in vowel: 
        count=count+ 1
print("count the vowel",count)

# counting the consonent

# vowel = ['a','e','i','o','u']
# word = 'programming'
# count=0
# for character in word:
#     if character not in  vowel:
#         count+= 1
# print(count)