#All basic logic gates made only using NAND Gates

def AND(a, b):
    return a & b
def NOT(a):
    return ~a + 2
def NAND(a, b):
    return NOT(AND(a, b))



#NOT
print("Output of NOT 0 is", NAND(0, 0))
print("Output of NOT 1 is", NAND(1, 1), "\n")

#NAND
print("Output of 0 NAND 0 is", NAND(0, 0))
print("Output of 0 NAND 1 is", NAND(0, 1))
print("Output of 1 NAND 0 is", NAND(1, 0))
print("Output of 1 NAND 1 is", NAND(1, 1), "\n")

#AND
print("Output of 0 AND 0 is", NAND(1, 1))
print("Output of 0 AND 1 is", NAND(1, 1))
print("Output of 1 AND 0 is", NAND(1, 1))
print("Output of 1 AND 1 is", NAND(0, 0), "\n") 

#OR
print("Output of 0 OR 0 is", NAND(1, 1))
print("Output of 0 OR 1 is", NAND(0, 0))
print("Output of 1 OR 0 is", NAND(0, 0))
print("Output of 1 OR 1 is", NAND(0, 0), "\n") 

#NOR
print("Output of 0 NOR 0 is", NAND(0, 0))
print("Output of 0 NOR 1 is", NAND(1, 1))
print("Output of 1 NOR 0 is", NAND(1, 1))
print("Output of 1 NOR 1 is", NAND(1, 1), "\n") 

#XOR
print("Output of 0 XOR 0 is", NAND(1, 1))
print("Output of 0 XOR 1 is", NAND(0, 0))
print("Output of 1 XOR 0 is", NAND(0, 0))
print("Output of 1 XOR 1 is", NAND(1, 1))
