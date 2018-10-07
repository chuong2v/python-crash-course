import calculator
from Dog import Dog

numbers = [1,3,4,5,6]

add = calculator.add(*numbers)
  
print("add:", add)
mul = calculator.mul(*numbers)
print("multiply:", mul)
bi = Dog("Bi", 2)
bi.walk()
print(bi.age)