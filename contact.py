import sqlite3

print("[1] Add a contact. ")
print("[2] view all contacts. ")
print("[3] modify a contact .")
print("[4] delete a contact .")
print("")
select = input("[*] select an option 1 to 4: ")

conn = sqlite3.connect("phonebook.db")
curs = conn.cursor()
curs.execute("CREATE TABLE IF NOT EXISTS contacts (name text,phoneNumbe integer,email text)")
conn.commit()

if int(select) == 1:
    name = input("enter the name: ")
    number = input("enter the phone number: ")
    email = input("enter email: ")
    curs.execute(f"INSERT INTO contacts VALUES('{name}',{number},'{email}')")
    conn.commit()

if int(select) == 3:
    update_name = input("[*] which contact do you want to update: ")
    new_name = input("[*] enter the new name: ")
    curs.execute(f"UPDATE contacts SET name = '{new_name}' where name = '{update_name}' ")
    conn.commit()

if int(select) == 2 :
    curs.execute("SELECT * FROM  contacts")
    data = curs.fetchall()
    for cont in data:
        print(cont)