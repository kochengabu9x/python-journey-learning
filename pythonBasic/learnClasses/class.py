# starting belajar class
class Student:
    def __init__(self, name, age, fav):
        self.name = name
        self.age = age
        self.fav = fav
    
    def printInf(self, *mInf):
        print(f"my name is {self.name}, my age is {self.age}, and my favorite activity is {self.mark}")
        
        if mInf: 
            print("and my other information is: ")
            for x in mInf:
                print(x)
   
# fungsi sendiri ga ada kelas nya     
def otherInfo():
        otrInfo = []
        print("berikan list makanan favorit kamu, ketika selesai tekan x")
        
        while True : 
            user_input = input("")
            
            if user_input == "x":
                break
            otrInfo.append(user_input)
            
        return otrInfo
                
# belajar atribut private cara set dan get nya juga sekalian                
class Speed: 
    def __init__(self):
        self.__newSpeed = 10
        self.speed = 30
    
    def getNewSpeed(self):
        return self.__newSpeed
    
    def setNewSpeed(self, newSpeed):
        self.__newSpeed = newSpeed
        
#belajar public dan private method
class Example:
    def __init__(self):
        self.x = 10
        self._y = 20
        self.__z = 30
    
    def publicMethod(self):
        print(self.x)
        print(self._y)
        print(self.__z)
        self.__privateMethod()
    
    def __privateMethod(self):
        print("this is the inside of private method")
        
        
        



"""
a = Example()
print(a.publicMethod()) 

s = Speed()
s.setNewSpeed(900)
print(s.getNewSpeed())

name  = input("what's your name? ")
age = int(input("what's your age? "))
fav = input("what's your favorite class? ")

demoStd = Student(name,age,fav)

info = otherInfo()

demoStd.printInf(info)
"""
