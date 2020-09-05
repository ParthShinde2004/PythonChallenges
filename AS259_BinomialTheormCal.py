import math

print("(a+bX)^c")
a = int(input('a ='))
b = int(input('b ='))
c = int(input('c ='))

x = 2
expansion = str(a**c) + ' + ' + str(b*c) + 'x'
while x < (c+1):
    nCr = (math.factorial(c)) / ((math.factorial(x)) * (math.factorial(c-x)))
    expansion = expansion + ' + ' + str((c**x) * int(nCr)) + 'x^' + str(x)
    x = x + 1
print(expansion)
