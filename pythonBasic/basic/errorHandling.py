result = None
x = int(input("input number 1: "))
y = int(input("input number 2: "))

try :
    result = x/y
except Exception as e : 
    print("something is error", e)  
else :
    print("ga error jadi excecute ini")
    print("the result is: ", result)
finally:
    print("mau apapun kondisinya bakal di eksekusi setelah semuanya")

