 # method overloading

class A:
    def show(self):
        print('welcome')


    def show(self,firstname=" "):
        print('welcome',firstname)


    def show(self,firstname=" ",lastname = " "):
        print('welcome',firstname,lastname )

am=A()
am.show()
am.show("india","bharat")
am.show()


# method overriding 

class A:                    # parent class
    def disp(self):
        print(" This is parent class ", "ram")

class B(A):                  # child class parent class ko child class access karne k liye super() methode ka use hota hai
    def disp(self):
        super().disp()
        print(" This is child class ")

am2 =B()
am2.disp()