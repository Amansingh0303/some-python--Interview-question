class A:
    _a=10    #protected
    __b= 30  #private
    def show(self):
        print('a',self._a)
        print('b',self.__b)
obj=A()
obj.show()
print("outside of class ",obj._a) #class baher private variable ko access nhi kar sakte protected variable ko usi class member k throught access kar sakte hai
print("outside of class ",A._a) 
