import sqlite3
import re 


print("[1] Add a contact. ")
print("[2] view all contacts. ")
print("[3] modify a contact .")
print("[4] delete a contact .")
print("")
select = input("[*] select an option 1 to 4: ")

while (not select.isdigit()) or (int(select) > 4):
    select = input("[*] select an option 1 to 4: ")

conn = sqlite3.connect("phonebook.db")
curs = conn.cursor()
curs.execute("CREATE TABLE IF NOT EXISTS contacts (name text,phoneNumbe integer,email text)")
conn.commit()


curs.execute("SELECT * FROM  contacts")
data = curs.fetchall()
arr = []
for i in data:
    for j in i:
        arr.append(j)
if int(select) == 1:
    name = input("enter the name: ")
    number = input("enter the phone number: ")
    while (len(number) != 10) or (not number.isdigit()):
       print("please enter a valid number")
       number = input("enter the phone number: ") 
    email = input("enter email: ")
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while not re.match(pat,email):
        print("enter a valid email")
        email = input("enter email: ")
    curs.execute(f"INSERT INTO contacts VALUES('{name}',+254{number},'{email}')")
    conn.commit()
    print('''
    *****************contact saved sucessfully*****************
    ''')
    

if int(select) == 3:
    update_name = input("[*] which contact do you want to update: ")
    if update_name in arr:
        new_name = input("[*] enter the new name: ")
        curs.execute(f"UPDATE contacts SET name = '{new_name}' where name = '{update_name}' ")
        conn.commit()
        print("contact updated succesfully")
    else:
        print("The name was not in the contacts!")

if int(select) == 2 :
    curs.execute("SELECT * FROM  contacts")
    data = curs.fetchall()
    count = 1
    for cont in data:
        print(f"[{count}] Name: {cont[0]} Number: {cont[1]}  Email: {cont[2]}")
        count += 1

if select == "4":
    delete = input("enter the name of the contact you want to delete: ")
    if delete in arr:
        curs.execute(f"DELETE FROM contacts WHERE name = '{delete}'")
        conn.commit()
    else:
        print("record does not exist!")

    print("**************contact deleted successfuly ***********************")


