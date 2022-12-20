print(
    """
   _ _ _ _ _ _     _ _ _ _ _ _ 
  |    _ _   |    |           |
  |   |   |  |    |    _ _ _ _|
  |   |_ _|  |    |   |
  |          |    |   |
  |   _ _ _ _|    |   |
  |   |           |   |_ _ _ _
  |   |           |           |
  |_ _|           |_ _ _ _ _ _|


    """
)

import random
#menu
print("[1] check my password strength. ")
print("[2] generate password. ")
print("[3] strengthen my passwod .")
print("")


choice = input("[ * ]select option: ")
if type(choice) == 'int':
    while int(choice)  >= 4 :
       choice = input("[ * ]select option: ")
else:
     while type(choice)  == 'str':
       choice = input("[ * ]select option: ")
# variables (global)
nums = [1,2,3,4,5,6,7,8,9,0]
spChars = ["!","@","#","$","%","&","*","(",")","_","+","-",";","<",":","|","'\'","?","/",">","."]
smallAlphabet = []
capsAlaphabet = []
for c in range(97, 123):
    smallAlphabet.append(chr(c))
for c in range(65, 91):
    capsAlaphabet.append(chr(c))
  
########  chacking the strength of the password 

def strengthCheck(password):
    pas = list(password)
    capsl = 0
    numbers = 0
    spchar = 0

    for letter in pas:
            if letter.isupper():
                capsl += 1
            if letter.isdigit():
                numbers += 1
            if letter in spChars:
                spchar += 1
    
    if 6 < len(pas) < 10 :
        if  numbers <= 0 and capsl <= 0  and spchar <= 0:
            print("weak password")
        if  numbers == 1 or capsl == 1  or spchar == 1:
            print("strong password") 
        if  numbers >= 2 or capsl >= 2  or spchar >= 2:
            print("stronger password")
    if len(pas) >= 10:

        if  numbers <= 0 and capsl <= 0  and spchar <= 0:
            print("good password")
        if  numbers == 1 or capsl == 1  or spchar == 1:
            print("stronger password") 
        if  numbers >= 2 or capsl >= 2  or spchar >= 2:
            print("strongest password")
    else:
        print("your password length is below six char (weak)")

########  generating a new password

def generatePasscode(length):
    rand_num = random.sample(nums,round(int(length)/4))
    rand_spchar = random.sample(spChars,round(int(length)/4))
    rand_smletters = random.sample(smallAlphabet,round(int(length)/4))
    rand_capsletters = random.sample(capsAlaphabet,round(int(length)/4))
    join = rand_capsletters+rand_num+rand_spchar+rand_smletters
    password = random.sample(join,len(join))
    passcode = ''.join(map(str,password))
    

    print(f"your password is ---> {passcode}")

############    streangthening the password 

def strengthenPassword(password):
    if strengthCheck(password) == 'good password':
        print ("yes")

## checking input choices

if int(choice) == 1:
     print("""
     
                        Disclaimer !!!!!  this does not check common passwords like 123456789
                                        ! we are working on that
                                                 stay safe

     """)
     havePass=input("Enter your password: ")
     strengthCheck(havePass)
if int(choice) == 2:
     length=input("How long do you want your password to be: ")
     generatePasscode(length)
if int(choice) == 3:
    password = input("input your curent password: ")
    strengthenPassword(password)

    