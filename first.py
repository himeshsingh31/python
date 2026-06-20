from array import array
from numpy import *


s = 1
while s<10:
 print(s)
 s +=1



x =2
while x<10:
    x += 1
    if x>5:
        break
    print(x)
print("out of loop")   


arr = array([0,30,45,60,90],int)
arr1 = deg2rad(arr)
arr2 = sin(arr1)

print(arr)
print(arr2)


class car: 
    def __init__(self,color):
        self.color = color

    def printer(xyz):
        print(xyz.name)   




c1 = car('red')
c2 = car('blue')

c1.name = 'himesh'
c2.age = 18


print(c2.age)
print(c1.color)
print(c1.printer())
c1.printer()


