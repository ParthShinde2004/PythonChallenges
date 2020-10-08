import random

ChoicePassword = input("What do you want you password to be? (Colour/Place/Animal)")
Animal = ["Dog", "Cat"]
Colour = ["Red", "Blue"]
Place = ["Tokyo", "KL"]
SpecialCharacters = ["@", "/", ";", "%", "*", "&", ".", ",", "#"]

def generating_password():
    if ChoicePassword == "Animal":
        Password = random.choice(Animal) + random.choice(SpecialCharacters)
    elif ChoicePassword == "Colour":
        Password = random.choice(Colour) + random.choice(SpecialCharacters)
    else:
        Password = random.choice(Place) + random.choice(SpecialCharacters)
    print(Password)

while ChoicePassword != "Place" or ChoicePassword != "Colour" or ChoicePassword != "Animal":
    print("Enter a value input")
    ChoicePassword = input("What do you want you password to be? (Colour/Place/Animal)")

generating_password()
