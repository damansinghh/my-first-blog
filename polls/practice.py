#!/usr/bin/python


class Parent:
    def __myMethod(self):
      print ('Calling parent method')


class Child(Parent): # define child class
   def __myMethod(self):
      print ('Calling child method')
      self.__method()


c = Child()          # instance of child
c.myMethod()         # child calls overridden method
