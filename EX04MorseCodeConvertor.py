def morse(txt):
    encrypt = {'A':'.-', 'B':'-...', 'C':'-.-.',
               'D':'-..', 'E':'.', 'F':'..-.',
               'G':'--.', 'H':'....', 'I':'..',
               'J':'.---', 'K':'-.-', 'L':'.-..',
               'M':'--', 'N':'-.', 'O':'---',
               'P':'.--.', 'Q':'--.-', 'R':'.-.',
               'S':'...', 'T':'-', 'U':'..-',
               'V':'...-', 'W':'.--', 'X':'-..-',
               'Y':'-.--', 'Z':'--..', ' ':'.....'}
    decrypt = {v: k for k, v in encrypt.items()}

    if '-' in txt:
        return ''.join(decrypt[i] for i in txt.split())
    return ' '.join(encrypt[i] for i in txt.upper())
while True:
    try:
        menu = int(input("Type 1 if you wish to use the translator, or type 2 if you want to exit the program:"))
        if (menu == 1):
            inputs = input("Input what you would like to be converted:")
            print(morse(inputs))
            break
        elif (menu ==2):
            break
    except ValueError:
        print("Error: Please go again")
