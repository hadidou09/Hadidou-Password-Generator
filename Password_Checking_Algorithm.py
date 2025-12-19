# Assigning all the needed characters in a password
uppercases = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
lowercases = ['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','e','y','u','i','o','a']
digits = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*',')','(','_','=','+','\'','\"','.',',',';',':','?','/','<','>','`','~','[',']','{','}','|']
strength = ''

def length_check(word):# Counting the number of characters in a password
    count = 0
    for i in word:
        count += 1
    if count >= 8:
        return True
    else:
        return False
    
def pattern_check(word):# Counting number of patterns and defining the password strength
    number_of_symbols = 0
    number_of_digits = 0
    number_of_lowercases = 0
    number_of_uppercases = 0
    for char in word:# Counting number of patterns
        if char in uppercases:
            number_of_uppercases += 1
        elif char in lowercases:
            number_of_lowercases += 1
        elif char in digits:
            number_of_digits += 1
        else:
            number_of_symbols += 1
    # Counting strength points
    strength_points = 0
    if number_of_uppercases >= 1:
        strength_points += 1
    if number_of_digits >= 1:
        strength_points += 1
    if number_of_symbols >= 1:
        strength_points += 1
    if number_of_lowercases >= 1:
        strength_points +=1 
    # Defining the password strength
    if strength_points > 2:
        return True
    else:
        return False

def single_password_check():
    password = str(input("Please enter the password:"))
    # Assigning the strength check for the password
    if length_check(password) == False:
      strength = 'Weak'
      return print(f"The password given \'{password}\' is {strength}.")
    else:
      if pattern_check(password) == True:
          strength = 'Strong'
          return print(f"The password given \'{password}\' is {strength}.")
      else:
          strength = 'Weak'
          return print(f"The password given \'{password}\' is {strength}.")

def passwords_list_check():
    filename = str(input('Please enter the password list path:'))
    
    print("A text file was created for every passowrd with its strength check by the name \'strength_check.txt\'.")
    file_handle1 = open(filename,'r')
    file_handle2 = open("strength_check.txt",'w')# Creating a new list of passwords with their strength check
    for password in file_handle1:# Assigning the passwords status for every password
        password = password.strip()
        if length_check(password) == False:
          strength = 'Weak'
          file_handle2.write(password+ " ------> "+ strength+"\n")
        else:
          if pattern_check(password) == True:
              strength = 'Strong'
              file_handle2.write(password+" ------> "+strength+"\n")
          else:
              strength = 'Weak'
              file_handle2.write(password+" ------> "+strength+"\n")
    

              



