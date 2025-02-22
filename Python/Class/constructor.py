class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def greet(self):
        print("Greetings ",self.name)
    
p1 = Person("John",30)
print(p1.name," ",p1.age)
p1.greet()