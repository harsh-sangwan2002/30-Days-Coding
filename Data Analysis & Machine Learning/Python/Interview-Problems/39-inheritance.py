class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, my name is {self.name}")
        
        
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        
student1 = Student("John", 36, 1234)
student2 = Student("Jane", 25, 5678)
student3 = Student("Alice", 30, 91011)

student1.greet()
student2.greet()
student3.greet()