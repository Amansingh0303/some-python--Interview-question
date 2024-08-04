
while True:
    no1=int(input("Enter the First no: "))
    no2=int(input("Enter the Second no: "))
    print("1.Addition\n2.Subtraction\n3.multiplication\n4.divison")
    choice= int(input("Choose the from above: "))
    if choice==1:
        print("Addition is :", no1+no2 )
    elif choice==2:
        print("Subtraction is :", no1-no2 )
    elif choice==3:
        print("Multiplication is :", no1*no2 )
    elif choice==4:
        print("Divison is :", no1/no2 )

    else:
        print("Ivalid choice")
    ans=input("Do want to continue(y/n)")
    valid=ans.lower()
    if valid!="y":
        break
    


