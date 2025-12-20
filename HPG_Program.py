import Password_Generation_Algorithm
import Password_Checking_Algorithm
# Importing the created modules 


def password_list():
  while True: # Length choice loop
   choice_of_length = input('Do you want the passwords to have a specific length?\n[Y/N]:').upper()
   if choice_of_length == 'Y':

    while True: # The length loop
      try:
       length = int(input('Enter the length of the passwords you want:'))
       if  length <= 0 :
         print('Invalid input, please try again.')
         continue # continuing the length loop
      except ValueError:
        print('Invalid input, please try again.')
        continue # continuing the length loop
      break # Breaking the length loop

    while True: # Number of passwords loop
      try:
       number_of_passwords = int(input('Enter the number of passwords you want:'))
       if  number_of_passwords <= 0 :
         print('Invalid input, please try again.')
         continue # continuing number of passwords loop
      except ValueError:
        print('Invalid input, please try again.')
        continue # continuing number of passwords loop
      break # breaking number of passwords loop

    while True: # Symbols choice loop
      choice_2 = input('Do you want the passwords to have symbols?\n[Y/N]:').upper()
      if choice_2 == 'Y':
        Password_Generation_Algorithm.password_list_generator_with_length_with_symbols(length,number_of_passwords)
        print("-"*100)
        break # Breaking symbols choice loop
      elif choice_2 == 'N':
        Password_Generation_Algorithm.password_list_generator_with_length_without_symbols(length,number_of_passwords)
        print("-"*100)
        break # Breaking symbols choice loop
      else:
        print("Invalid input, please try again.")
        continue # continuing symbols choice loop
    break # Breaking the length choice loop
     
   elif choice_of_length == 'N':
    while True: # Number of passwords loop
      try:
       number_of_passwords = int(input('Enter the number of  passwords you want:'))
       if  number_of_passwords <= 0 :
         print('Invalid input, please try again.')
         continue # continuing number of passwords loop
      except ValueError:
        print('Invalid input, please try again.')
        continue # continuing number of passwords loop
      break # breaking number of passwords loop

    while True: # Symbols choice loop
      choice_2 = input('Do you want the passwords to have symbols?\n[Y/N]:').upper()
      if choice_2 == 'Y':
        Password_Generation_Algorithm.password_list_generator_without_length_with_symbols(number_of_passwords)
        break # Breaking symbols choice loop
      elif choice_2 == 'N':
        Password_Generation_Algorithm.password_list_generator_without_length_without_symbols(number_of_passwords)
        break # Breaking symbols choice loop
      else:
        print("Invalid input, please try again.")
        continue # continuing symbols choice loop
    print("-"*100)
    break # Breaking the length choice loop
   
   else:
     print('Invalid input, please try again.')
     continue # continuing the length choice loop
 

def single_password():
    # The length loop 
    while True:
     try:
      length = int(input('Enter the length of the password you want:'))
      if  length <= 0 :
        print('Invalid input, please try again.')
        continue
     except ValueError:
       print('Invalid input, please try again.')
       continue
     break # Breaking The length loop

    # the symbols choice loop
    while True:
     choice_2 = input('Do you want the password to have symbols?\n[Y/N]:').upper()
     if choice_2 == 'Y':
       Password_Generation_Algorithm.single_password_generator_with_symbols(length)
       print("-"*100)
       break # Breaking the symbols choice loop
     elif choice_2 == 'N':
       Password_Generation_Algorithm.single_password_generator_without_symbols(length)
       print("-"*100)
       break # Breaking the symbols choice loop
     else:
       print("Invalid input, please try again.")
       continue # continuing the symbols choice loop
     

def password_checker():
  # The type choice loop
  while True:
    choice = str(input("If you want to check a single password enter [S]\nAnd if you want to check a TXT list of password enter [L]\n[S/L]:")).upper()
    if choice == 'S':
      Password_Checking_Algorithm.single_password_check()
      print("-"*100)
      break # Breaking the type choice loop
    elif choice == 'L':
      Password_Checking_Algorithm.passwords_list_check()
      print("-"*100)
      break # Breaking the type choice loop
    else:
      print("Invalid input, please try again.")
      continue # Continuing type choice loop
  
     
def main_program():
    print('        _        _   ________     ________      ')
    print('       | |      | | |  ____  |  _| _____  |_    ')
    print('       | |      | | | |____| | |  |     |___|   ')
    print('       | |______| | | _______| |  |             ')
    print('       |  ______  | | |        |  |     ____    ')
    print('       | |      | | | |        |  |    |_   |   ')
    print('       | |      | | | |        |__ |_____|  |   ')
    print('       |_|      |_| |_|          |__________|   ')
    print('************ Hadidou Password Generator v1.0 ************')
    while True: # Generation type loop
     choice = input('If you want a single password generator enter [S]\nOtherwise if you want to generate a list of password enter [L]\nOr if you want to check the strength of your password enter [C]\n[S/L/C]:').upper()
     if choice == 'S':
        single_password()
     elif choice == 'L':
        password_list()
     elif choice == 'C':
        password_checker()
     else:
        print('Invalid input, please choose again.')
        continue # Continuing type choice loop
     

if __name__ == '__main__': # executing the main_program when executing this module
  main_program()

