# compotision relationship "part of" (Content in container) strong connection dependent of each other

class Salary:
    def __init__(self, pay, reward, bonus):
        self.pay = pay
        self.reward = reward
        self.bonus = bonus
    
    def annual_salary(self):
        return (self.pay*12) + self.reward + self.bonus 
    
class Employee:
    def __init__(self, name, position, pay, reward, bonus):
        self.name = name
        self.position = position
        self.final_salary = Salary(pay,reward,bonus)
        
    def final_salary_m(self):
        return self.final_salary.annual_salary()
    

emp = Employee("amalia", "PO", 10000, 5000, 20000)
print(emp.final_salary_m())

# Aggregation relation "has" the object is independent, weak connection

class Salary:
    def __init__(self, pay, reward, bonus):
        self.pay = pay
        self.reward = reward
        self.bonus = bonus
    
    def annual_salary(self):
        return (self.pay*12) + self.reward + self.bonus 
    
class Employee:
    def __init__(self, name, position, sal):
        self.name = name
        self.position = position
        self.final_salary = sal
        
    def final_salary_m(self):
        return self.final_salary.annual_salary()
    
sal = Salary(10000,1000,2000)
emp = Employee("amalia", "PO", sal)

print(emp.final_salary_m())