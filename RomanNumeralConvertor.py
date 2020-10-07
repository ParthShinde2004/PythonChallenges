"""This is a Roman Numeral and Integer converter that can convert number from roman to denary and back from 0-3999"""

RomanValues =	{
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000,
}

def roman_to_int(str):
    total = 0
    i = 0

    while (i < len(str)):
        s1 = RomanValues[str[i]]
        if (i+1 < len(str)): 
            s2 = RomanValues[str[i+1]]
            if (s1 >= s2): 
                total = total + s1 
                i = i + 1
            else: 
                total = total - s1 
                i = i + 1
        else: 
            total = total + s1 
            i = i + 1
    return total

def int_to_roman(number): 
    numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000] 
    symbols = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"] 
    j = 12
    while number: 
        div = number // numbers[j] 
        number %= numbers[j] 
  
        while div: 
            print(symbols[j], end = "") 
            div -= 1
        j -= 1

RomanNum = str(input("What is the roman value you want to convert? (Enter No if you want to convert integer)"))
if RomanNum == "No":
    number = int(input("What is the integer value you want to convert?"))
    int_to_roman(number)
else:
    print(roman_to_int(RomanNum))
