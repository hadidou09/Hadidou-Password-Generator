import secrets
data = [
    ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','e','y','u','i','o','a','0','1','2','3','4','5','6','7','8','9'],
    ['!','@','#','$','%','^','&','*',')','(','_','=','+','\'','\"','.',',',';',':','?','/','<','>','`','~','[',']','{','}','|']
]# All characters used for password generating

def single_password_generator_with_symbols(length:int):
    password = '' # Aligning new password variable
    for i in range(length):
        data_type = secrets.randbelow(2) # choosing data type      
        if data_type == 0 :
            number_choice = secrets.randbelow(62) # Choosing the exact character
            data_choice = data[0][number_choice] 
            password = password + data_choice # Generating a password
        elif data_type == 1:
            number_choice = secrets.randbelow(30) # Choosing the exact character
            data_choice = data[1][number_choice]
            password = password + data_choice # Generating a password
    return print('Your password is:', password)

         

def single_password_generator_without_symbols(length:int):
    password = '' # Aligning new password variable
    for i in range(length):
        number_choice = secrets.randbelow(62) # Choosing the exact character
        data_choice = data[0][number_choice]
        password = password + data_choice # Generating a password
    return print('Your password is:', password)



def password_list_generator_with_length_with_symbols(length:int,number_of_passwords:int):
    filename = input('Enter the full name of your text (with the extension if it is already created):') # Creating or choosing a file
    file_handle = open(filename,'w')
    for i in range(number_of_passwords):
      password = '' # Aligning new password variable
      for i in range(length):
          data_type = secrets.randbelow(2) # choosing data type       
          if data_type == 0 :
              number_choice = secrets.randbelow(62) # Choosing the exact character
              data_choice = data[0][number_choice]
              password = password + data_choice # Generating a password
          elif data_type == 1:
              number_choice = secrets.randbelow(30) # Choosing the exact character
              data_choice = data[1][number_choice]
              password = password + data_choice # Generating a password
      file_handle.write(password + '\n') # Writing on the file
    return print(f'Your text file {filename} is ready with {number_of_passwords} passwords.')



def password_list_generator_with_length_without_symbols(length:int,number_of_passwords:int):
    filename = input('Enter the full name of your file (with the extension if it is already created):') # Creating or choosing a file
    file_handle = open(filename,'w')
    for i in range(number_of_passwords):
      password = '' # Aligning new password variable
      for i in range(length):
        number_choice_2 = secrets.randbelow(62) # Choosing the exact character
        data_choice_2 = data[0][number_choice_2]
        password = password + data_choice_2 # Generating a password
      file_handle.write(password + '\n') # Writing on the file
    return print(f'Your text file {filename} is ready with {number_of_passwords} passwords.')




def password_list_generator_without_length_with_symbols(number_of_passwords:int):
    filename = input('Enter the full name of your file (with the extension if it is already created):') # Creating or choosing a file
    file_handle = open(filename,'w')
    for i in range(number_of_passwords):
      password = '' # Aligning new password variable
      length = secrets.randbelow(12)+5 # Choosing a random length
      for i in range(length):
          data_type = secrets.randbelow(2) # choosing data type       
          if data_type == 0 :
              number_choice_2 = secrets.randbelow(62) # Choosing the exact character
              data_choice_2 = data[0][number_choice_2]
              password = password + data_choice_2 # Generating a password
          elif data_type == 1:
              number_choice_2 = secrets.randbelow(30) # Choosing the exact character
              data_choice_2 = data[1][number_choice_2]
              password = password + data_choice_2 # Generating a password
      file_handle.write(password + '\n') # Writing on the file
    return print(f'Your text file {filename} is ready with {number_of_passwords} passwords.')




def password_list_generator_without_length_without_symbols(number_of_passwords:int):
    filename = input('Enter the full name of your file (with the extension if it is already created):') # Creating or choosing a file
    file_handle = open(filename,'w')
    for i in range(number_of_passwords):
      password = '' # Aligning new password variable
      length = secrets.randbelow(12)+5 # Choosing a random length
      for i in range(length):     
              number_choice = secrets.randbelow(62) # Choosing the exact character
              data_choice = data[0][number_choice]
              password = password + data_choice # Generating a password
      file_handle.write(password + '\n') # Writing on the file
    return print(f'Your text file {filename} is ready with {number_of_passwords} passwords.')
