import random

class Character:
    def __init__(self):
        self.name = ""
        self.attack = 0
        self.defence = 0
        self.__health = 0
        self.experience = 0

    def print_basics(self):
        print("\nName:      ",self.name)
        print("Attack:     ",self.attack)
        print("Defence     ",self.defence)
        print("Health:     ",self.__health)
        print("Experience: ",self.experience)

    def setter(self,name):
        self.name = name
        self.attack = random.randint(0,50)
        self.defence = random.randint(0,50)
        self.__health = random.randint(30,50)

    def health_getter(self): 
        return self.__health

    def print_me(self):
        self.print_basics()


class wizard(Character):
    def __init__(self):
        Character.__init__(self)
        self.magic = 30

    def print_me(self):
        self.print_basics()
        print("Magic       ",self.magic)

class knight(Character):
    def __init__(self):
        Character.__init__(self)
        self.armour = 30

    def print_me(self):
        self.print_basics()
        print("Armour      ",self.armour)

Arthur = knight()
Arthur.setter("Arthur")
Arthur.print_me()

Merlin = wizard()
Merlin.setter("Merlin")
Merlin.print_me()

caste = input("\nWould you like to be a Wizard or Knight?")
char_name = input("And what is your name?")

if caste.upper() == "K":
    print("A great knight is created!")
    you = knight()
elif caste.upper() == "W":
    print("A great wizards shimmers into existance")
    you = wizard()
else:
    print("\nTyping Wizard or Knight is too much for you! \nClearly you plan to die...\nBasic peasant for you!")
    you = Character()

you.setter(char_name)
you.print_me()
