def add(*numbers):
  return sum(numbers)

def mul(*numbers):
  a = 1
  for number in numbers:
    a *= number
  return a


