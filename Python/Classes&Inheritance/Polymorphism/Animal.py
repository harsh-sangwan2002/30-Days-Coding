class Animal:
    def make_sound(self):
        print("Unknown sound")
        
class Dog(Animal):
    def make_sound(self):
        print("Bark")
    
class Cat(Animal):
    def make_sound(self):
        print("Meow")
        
dog = Dog()
cat = Cat()
goat = Animal()

dog.make_sound()
cat.make_sound()
goat.make_sound()