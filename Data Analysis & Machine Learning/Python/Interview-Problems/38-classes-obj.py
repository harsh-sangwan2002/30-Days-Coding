class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, my name is {self.name}")
        
        
person1 = Person("John", 36)
person2 = Person("Jane", 25)
person3 = Person("Alice", 30)

person1.greet()
person2.greet()
person3.greet()