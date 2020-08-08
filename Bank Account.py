# Python code to validate user on below conditions for Sign up . (required : username , password , a/c no , DOB)

#Username should contain a minimum 8 characters and no spaces.
#A/C number should contain numbers only . 
#DOB should be in format "ddmmyyyy" 
#if any check fails , prompt user to correct them .  If all okay , return 'Done' message . 



import re
from datetime import datetime
print(("Enter Username,Password,Account number and DOB respectivily"))



while True:
        Username = input("Enter Username: ")
        if len(Username) < 8:
            print("Make sure your Username is at least 8 letters long")
        elif ' ' in Username:
            print(" Ensure there is no space")
        else:
            print("Your Username seems fine, DONE")
            break


Password = input("Enter a password: ")



while True:
      AccountNo = input("Enter Account number: ")
      if AccountNo.isdigit() is False:
        print("Make sure your Account has only number in it")
      else:
        print("Account number is valid")
        break




while True:
  i = str(input('date'))
  try:
    dt_start = datetime.strptime(i, '%d%m%Y')
    break
  except ValueError:
    print ("Incorrect format")
    
    

print("Username:", Username)
print("Password:", Password)
print("Account number:", AccountNo)
print("DOB:", i)