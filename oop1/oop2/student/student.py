#student.py
class Student:
   
     # protected data members
     _stuid = None
     _name = None
     _major = None
   
     # constructor
     def __init__(self, stuid,name, major):
         self._stuid = stuid
         self._name = name
         self._major = major
   
     # protected member function  
     def _displayNameAndMajor(self):
 
          # accessing protected data members
          print("Name: ", self._name)
          print("Major: ", self._major)
