import datetime
import string
import random
import time

#Important Variables and Constants
Lives = 5
Score = 0
Boolean = "TRUE", "FALSE"
RandString = random.randint(2,10)

#Actual Quiz Game
def game():
  RightWrong = 0
  Question = random.choice(Choice)
  print(Question)
  Answer = input("What is the data type? (all lower case)")
  #This is for making the quiz happen
  if Question == str(Question):
    if Answer == "string":
      RightWrong = 1
      global Score += 1
    else:
      RightWrong = 0
  elif len(Question) == 1:
    if Answer == "char":
      RightWrong = 1
      global Score += 1
    else:
      RightWrong = 0
  elif Question == float:
    if Answer == "real":
      RightWrong = 1
      global Score += 1
    else:
      RightWrong = 0
  elif Question == "TRUE" or Question == "FALSE":
    if Answer == "Boolean":
      RightWrong = 1
      global Score += 1
    else:
      RightWrong = 0
  elif Question == int:
    if Answer == "integer":
      RightWrong = 1
      global Score += 1
    else:
      RightWrong = 0
  else:
    if Answer = "Date":
      RightWrong = 1
      global Score += 1
    else:
      RightWrong = 0
    
  #This is for lives and Scoring System
  if RightWrong == 0:
    if Lives == 0:
      
      print("Game Over!\nYour Score Was:", Score)
    else:
      Lives = Lives - 1
  else:
    print("Correct Answer")
    Lives = Lives
  pass

#Char Generator
def pseudocode_char_generator():
  letters = string.ascii_letters
  result_char = ''.join(random.choice(letters) for i in range(1))
  return (result_char)
  
#String Generator
def pseudocode_string_generator(length):
  letters = string.ascii_lowercase
  result_str = ''.join(random.choice(letters) for i in range(length))
  return (result_str)
  
#Real Generator
def pseudocode_real_generator():
  RandomReal = (random.randint(0,1000)/10)
  return RandomReal
  
#Boolean Generator
def pseudocode_boolean_generator():
  RandomBool = random.choice(Boolean)
  return RandomBool
  
#Integer Generator
def pseudocode_integer_generator():
  RandomNum = random.randint(0,100)
  return RandomNum
  
#Date Generator
def pseudocode_date_generator():
  startdate = datetime.date(2020, 1, 1)
  enddate = datetime.date(2020, 2, 1)
  time_between_dates = enddate - startdate
  days_between_dates = time_between_dates.days
  random_number_of_days = random.randrange(days_between_dates)
  random_date = startdate + datetime.timedelta(days=random_number_of_days)
  return random_date
  
#Prints all data types
def printeverything():
  print("Interger:",pseudocode_integer_generator())
  print("Real:",pseudocode_real_generator())
  print("Boolean:",pseudocode_boolean_generator())
  print("Date:",pseudocode_date_generator())
  print("String:",pseudocode_string_generator(RandString))
  print("Char:",pseudocode_char_generator())

#Randomises Questions
Choice = pseudocode_char_generator(), pseudocode_integer_generator(),pseudocode_real_generator(),pseudocode_boolean_generator(),pseudocode_date_generator(),pseudocode_string_generator(random.randint(2,10))

printeverything() #Gives examples for all data types 
game()
