#import necessary modules
from abc import ABC, abstractmethod

#create base class
class Absclass(ABC):

    #function to print a value
    def display(self,x):
        print("passed value: ", x)

    #abstract method
    @abstractmethod
    def task(self):
        print("we are inside Absclass task")

#create sub class
class test_class(Absclass):
    def task(self):
        print("we are inside test_class task")

#object of test_class created

hello = test_class()
hello.task()
hello.display(100)                    