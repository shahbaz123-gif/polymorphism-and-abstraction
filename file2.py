#import necessary peckages
from abc import ABC, abstractmethod
#create a base class
class Animal(ABC):

    #abstract method
    #should be implemented by all sub-classes
    def move(self):
        pass

#sub classes    
class Human(Animal):
    def move(self):
        print("i can walk and run")

class Snake(Animal):
    def move(self):
        print("i can crawl") 

class Dog(Animal):
    def move(self):
        print("i can bark")

class Lion(Animal):
    def move(self):
        print("i can roar")

hello =  Human() 
hello.move()

hi = Snake()
hi.move()

hey = Dog()
hey.move()

he = Lion()
he.move()