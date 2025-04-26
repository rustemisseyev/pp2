import psycopg2
import csv

conn = psycopg2.connect(
    dbname='yourdbname',
    user='yourusername',
    password='yourpassword',
    host='localhost',
    port='5432'
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    phone VARCHAR(20)
)
""")
conn.commit()

def insert_from_console():
    username = input("Enter username: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s) ON CONFLICT (username) DO UPDATE SET phone = EXCLUDED.phone", (username, phone))
    conn.commit()

def insert_from_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            username, phone = row
            cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s) ON CONFLICT (username) DO UPDATE SET phone = EXCLUDED.phone", (username, phone))
    conn.commit()

def update_user(username, new_phone):
    cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s", (new_phone, username))
    conn.commit()

def query(filter_name=None):
    if filter_name:
        cur.execute("SELECT * FROM phonebook WHERE username = %s", (filter_name,))
    else:
        cur.execute("SELECT * FROM phonebook")
    for row in cur.fetchall():
        print(row)

def delete_by_username(username):
    cur.execute("DELETE FROM phonebook WHERE username = %s", (username,))
    conn.commit()

def delete_by_phone(phone):
    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()

while True:
    print("\n1. Insert from console\n2. Insert from CSV\n3. Update\n4. Query\n5. Delete by username\n6. Delete by phone\n7. Exit")
    choice = input("Choose option: ")
    
    if choice == '1':
        insert_from_console()
    elif choice == '2':
        filename = input("Enter CSV filename: ")
        insert_from_csv(filename)
    elif choice == '3':
        username = input("Enter username to update: ")
        new_phone = input("Enter new phone: ")
        update_user(username, new_phone)
    elif choice == '4':
        f = input("Enter username to filter (or leave empty): ")
        query(f if f else None)
    elif choice == '5':
        username = input("Enter username to delete: ")
        delete_by_username(username)
    elif choice == '6':
        phone = input("Enter phone to delete: ")
        delete_by_phone(phone)
    elif choice == '7':
        break

cur.close()
conn.close()