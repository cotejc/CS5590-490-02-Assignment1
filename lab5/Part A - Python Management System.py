#Jeremiah Cote
#User Id -1
#Assignment/Lab 5
#Part A - Library Resource Management System
#13 July 2017

print("This is a program as a Library Resource Management System.\n")
class Person:
    #This is the first class of Person.  This will be used to Identify the person in the resource managment system
    def __init__(self, firstname, lastname):
        #This is the constructor, self needs to be included as this is object oriented, first name and last name are used to determine the input for the user
        self.firstname = input("Please enter first Name:")
        #This is to get input for the users first name
        self.lastname = input("Please enter last Name:")
        #This is to get input for the users last name
    def displayPerson(self):
        #This is used to define the function to display the inputs into the contents of the class
        print ("First Name : ", self.firstname, ",Last Name: ", self.lastname)
        #This is to print the contacts of the uses input within this class and it displays it to the screen to see

class Student(Person):
    #This is the second class of Student, but it is also used as an inhertiance from the Person class
    def __init__(self, stud):
        #This is the constructor used to determine the input for whether the person is a student or no
        self.stud = input("Are you a student, enter yes or no:")
        #This to identify the input answer for this class and to put it as a reference to itself.  This way when it is called it will identify what this vaule is
    def displayStudent(self):
        #This is used to define the function to display the inputs into the contents of the class
        print ("Student: ", self.stud)
        #This is to print the contacts of the uses input within this class and it displays it to the screen to see

class Librarian(Person):
    # This is the third class of Librarian, but it is also used as an inhertiance from the Person class
    def __init__(self, lib):
        # This is the constructor used to determine the input for whether the person is a student or no
        self.lib = input("Enter the Librarian's name:")
        #This to identify the input answer for this class and to put it as a reference to itself.  This way when it is called it will identify what this vaule is
    def displayLibrarian(self):
        #This is used to define the function to display the inputs into the contents of the class
        print ("Librarian: ", self.lib)
        #This is to print the contacts of the uses input within this class and it displays it to the screen to see

class __Fees:
    # This is the fourth class of Fees, but it is also a private member
    def __init__(self, owed):
        # This is the constructor used to determine the input for whether the person is a student or no
        self.owed = input("Do you owe any fees?:")
        #This to identify the input answer for this class and to put it as a reference to itself.  This way when it is called it will identify what this vaule is
    def displayFees(self):
        #This is used to define the function to display the inputs into the contents of the class
        print("Fees Owed: ", self.owed)
        #This is to print the contacts of the uses input within this class and it displays it to the screen to see

class Booklimit:
    # This is the fifth class of Booklimit
    def __init__(self, limit):
        # This is the constructor used to determine the input for whether the person is a student or no
        self.limit = input("Enter the name of the book checking out:")
        #This to identify the input answer for this class and to put it as a reference to itself.  This way when it is called it will identify what this vaule is
    def displayBooklimit(self):
        #This is used to define the function to display the inputs into the contents of the class
        print("Name of book checking out:", self.limit)
        #This is to print the contacts of the uses input within this class and it displays it to the screen to see

class Books(Student, Librarian):
    # This is the sixth class of Booklimit and also used as a multiple inheritance of the class person
    def __init__(self, mul):
        # This is the constructor used to determine the input for whether the person is a student or no
        self.mul = input("EPlease re-verify if the Person is a student and the Librarian's name:")
        #This to identify the input answer for this class and to put it as a reference to itself.  This way when it is called it will identify what this vaule is
    def displayBooks(self):
        # This is used to define the function to display the inputs into the contents of the class
        print("Student and Librarian Name:", self.mul)
        #This is to print the contacts of the uses input within this class and it displays it to the screen to see


class Manager(Person):
    pass
manager1= Manager("D Z, Z", 2000)
#This is used to have an ineritance to pass through and to output the information at a specific location.  It is passed we are only interested in getting
#the display information

class Manny(Student):
    pass
manny2 = Manny("I")
#This is used to have an ineritance to pass through and to output the information at a specific location.  It is passed we are only interested in getting
#the display information

class Lib (Librarian):
    pass
lib1 = Lib("L")
#This is used to have an ineritance to pass through and to output the information at a specific location.  It is passed we are only interested in getting
#the display information

class Fee (__Fees):
    pass
fee1 = Fee("L")
#This is used to have an ineritance to pass through and to output the information at a specific location.  It is passed we are only interested in getting
#the display information

class Book (Booklimit):
    pass
book1 = Book("L")
#This is used to have an ineritance to pass through and to output the information at a specific location.  It is passed we are only interested in getting
#the display information

class Multiple (Books):
    pass
lib2 = Books ("L")
#This is used to have an ineritance to pass through and to output the information at a specific location.  It is passed we are only interested in getting
#the display information

manager1.displayPerson()
#This is to display this particle sub class that reverts back to the main class
manny2.displayStudent()
#This is to display this particle sub class that reverts back to the main class
lib1.displayLibrarian()
#This is to display this particle sub class that reverts back to the main class
fee1.displayFees()
#This is to display this particle sub class that reverts back to the main class
book1.displayBooklimit()
#This is to display this particle sub class that reverts back to the main class
lib2.displayBooks()
#This is to display this particle sub class that reverts back to the main classmanager1.displayPerson()
#This is to display this particle sub class that reverts back to the main class
manny2.displayStudent()
#This is to display this particle sub class that reverts back to the main class
lib1.displayLibrarian()
#This is to display this particle sub class that reverts back to the main class
fee1.displayFees()
#This is to display this particle sub class that reverts back to the main class
book1.displayBooklimit()
#This is to display this particle sub class that reverts back to the main class
lib2.displayBooks()
#This is to display this particle sub class that reverts back to the main class


class1 = Person("Jeremiah", "Cote")
#This is to create in intance of Class 1
class2 = Student("Yes",)
#This is to create in intance of Class 2
class3 = Librarian("E",)
#This is to create in intance of Class 3
class4 = Books("No")
#This is to create in intance of Class 4
class5 = Booklimit("No")
#This is to create in intance of Class 5

class1.displayPerson()
#This is to call the instance of each class to display
class2.displayStudent()
#This is to call the instance of each class to display
class3.displayLibrarian()
#This is to call the instance of each class to display
class4.displayBooks()
#This is to call the instance of each class to display
class5.displayBooklimit()
#This is to call the instance of each class to display