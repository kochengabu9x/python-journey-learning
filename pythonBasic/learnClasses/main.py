from square import Square as sq
from triangle import Triangle as tq

s1 = sq()
s1.set_value(10,5)
s1.set_color("Blue")

print(s1.area(), s1.get_color()) 

t1 = tq()
t1.set_value(5,10)
t1.set_color("pink")

print(t1.area(), t1.get_color())
