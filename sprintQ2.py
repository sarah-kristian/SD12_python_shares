# Description: FizzBizz interview game
# Author:      Study Group 5
# Date:        2024-06-17


# import module
from message_handler import get_messages_fizzbizz

import time

# define functions

def FizzBizzOrigz(msgs):
  # original version of FizzBizz


  # define values for messages
  INTRO_ORIGZ = msgs["INTRO_ORIGZ"]
  GO_ON_MSG = msgs["GO_ON_MSG"]
  SIGN_OFF = msgs["SIGN_OFF"]

  # display output
  print(INTRO_ORIGZ)
  print(input(GO_ON_MSG))
  print()




  for num in range(1,101):
    if (num%5==0) and (num%8==0):
      print("FizzBizz")
      time.sleep(.2)
    elif num%5==0:
      print("Fizz")
      time.sleep(.1)
    elif num%8==0:
      print("Bizz")
      time.sleep(.1)
    
    else:
      print(num)
  print(SIGN_OFF)


def FizzBizzVarizz(msgs):
  # this is a program for the variant of fizzbizz

  # define values for messages
  INTRO_VARIZZ = msgs["INTRO_VARIZZ"]
  GO_ON_MSG = msgs["GO_ON_MSG"]
  SIGN_OFF = msgs["SIGN_OFF"]
  VALUE_PROMPT = msgs["VALUE_PROMPT"]
  WORD_PROMPT = msgs["WORD_PROMPT"]
  ERROR_WORDS = msgs["ERROR_WORDS"]
  ERROR_VALUE_RANGE = msgs["ERROR_VALUE_RANGE"]
  ERROR_VALUES = msgs["ERROR_VALUES"]   

  # runs variant of FizzBizz

  print(INTRO_VARIZZ)

  # get user inputs
         # get values
  while True:
      values = input(VALUE_PROMPT)
      filtered_values = ','.join(char for char in values if char.isdigit())
      values_list = [value for value in filtered_values.split(',')]
      if len(values_list) != 2:
          print(ERROR_VALUES)
      elif not all(char in "23456789," for char in filtered_values[0:3]):
          print(ERROR_VALUE_RANGE)
      else:
          value1, value2 = values_list
          break

         # get words
  while True:
      word_string = input(WORD_PROMPT).replace(" ", "")
      word_list = [word for word in word_string.split(',')]
      if len(word_list) != 3:
          print(ERROR_WORDS)
      else:
          word1, word2, word3 = word_list     # Assign each word to a separate variable
      break


  # display output
  print(input(GO_ON_MSG))
  for num in range(2,101):
      if (num%int(value1)==0) and (num%int(value2)==0):
          print(f"\n{word3.upper()}!!!\n")
          time.sleep(.2)
      elif num%int(value1)==0:
          print(f"{word1.lower()}")
          time.sleep(.1)
      elif num%int(value2)==0:
          print(f"{word2.lower()}")
          time.sleep(.1)
      else:
          print(num)


  #housekeeping
  print(SIGN_OFF)
  


def FizzBizzMenu():

  # determine language for messages
  fizzbizz_messages = get_messages_fizzbizz()

  CHOICE_PROMPT = fizzbizz_messages["CHOICE_PROMPT"]
  INVALID_CHOICE = fizzbizz_messages["INVALID_CHOICE"]

  # menu for choice of FizzBizz variants
  while True:
    choice = input(CHOICE_PROMPT)
    
    if choice == '1':
        print("\n\n-----------------Original------------------")
        FizzBizzOrigz(fizzbizz_messages)
    elif choice == '2':
        print("\n\n-----------------Variant------------------")
        FizzBizzVarizz(fizzbizz_messages)
    else:
        print(INVALID_CHOICE)

    while True:
      Continue=input("Do you want to continue (Y / N)? ").upper()
      if Continue != "Y" and Continue !="N":
        print("  Data Entry Error - Prompt to continue should be Y or N")
      else:
        break
    if Continue=="N":
      print(" Thank you for using our Program!")
      break
     


if __name__ == "__main__":
  FizzBizzMenu()