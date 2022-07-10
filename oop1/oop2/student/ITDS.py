#itds.py
from student import Student

# derived class
class ITDS(Student):
    # constructor
       def __init__(self, stuid,name, major):
                Student.__init__(self, stuid,name, major)
         
       # public member function
       def _displayNameAndMajor(self):
# accessing protected data members of super class
                print("ITDS Name: ", self._name)  
              
# accessing protected member functions of super class
                super()._displayNameAndMajor()


# creating objects of the derived class      
obj = ITDS("640108","Amorn", "Information Technology")
 
# calling public member functions of the class
obj.displeyDetails()
