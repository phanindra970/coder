class Person:
    def _init_ (self,name,age):
        self.name=name
        self.age=age
    def printName(self):
        print(self.name)
class Student(Person):
    def _init_ (self,name,age,regno):
        self.regno=regno
        super._init_(name,age)
    def printRegNo(self):
        print(self.regno)
s1=Student("Rahul",19,110);
s1.printRegNo()
s1.printName()
