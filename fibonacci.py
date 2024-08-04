# fib = [0,1]
# for i in range(5):
#     fib.append(fib[-1]+fib[-2])
# print(' '.join(str(e) for e in fib))


n = int(input("Enter the terms: "))
first=0
second=1
if n<=0:
    print("enter the positive integers")
elif n==1:
    print("Fibonacci series is:")
    print(first)
else:
    for i in range(n):
        print(first,end=" ")
        temp=first
        first=second
        second=temp+first 










