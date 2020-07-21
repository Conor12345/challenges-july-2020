#https://projecteuler.net/problem=65

from fractions import *

instructions = []
num = 2
while len(instructions) < 9:
    instructions += [1, num, 1]
    num += 2
print(instructions)
instructions.reverse()
x = Fraction(1, instructions.pop(0))
for struct in instructions:
    x = Fraction(1, x + struct)

x += 2
sum = 0
for char in str(x.numerator):
    sum += int(char)
print(sum)