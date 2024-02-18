class Student:
    def __init__(self):
        self.name = "amalia"
        self.age = 20
        self.mark = 70
        
    def talk(self):
        print(f"my name is {self.name}")
        print(f"my age is {self.age}")
        print(f"and my GPA is {self.mark}")
        
a1 = Student()

a1.name = "kocheng abu"

print(a1.name)
a1.talk()

