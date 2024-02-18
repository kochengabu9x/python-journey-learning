def sumf(x, y):
    c = x + y
    return c
    
num = sumf(10,5)

def sum(x,y):
    if type(x) == type(y):
        return x+y
    else :
        return "Data type nya beda" 

num1 = sum("amalia","yasmin")
print(num1)

def std (name, clas, **marks):
    print("Name :", name)
    print("class :", clas)
    print(marks)
    for x,y in marks.items():
        print(f"Pelajaran {x} nilainya {y}")
        
std("amalia","kucing", English = 10, Math = 11, Biology = 50, Fisika = 40, kimia = 70)