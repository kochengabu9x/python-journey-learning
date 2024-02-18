#input logic 1
age = int(input("umur berapa?"))

if age >= 18 and age <= 25:
    print("boleh pinjol")
else :
    print("tak boleh pinjol")
    
#input logic 2
number = int(input("masukin nomer: "))

if number >= 0:
    print("number is pawsitive")
    if number%2 == 0:
        print("number is even")
    else:
        print("number is odd")
else:
    print("number is meowgative")
    
