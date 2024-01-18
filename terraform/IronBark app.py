conn = sqlite3.connect('user_data.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table to store user data if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        birthday TEXT,
        ssn TEXT,
        maiden_name TEXT
    )
''')

# Save changes and close the connection
conn.commit()
conn.close()

def add_user(name, birthday, ssn, maiden_name):
    # Connect to the database
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    # Insert user data into the 'users' table
    cursor.execute('''
        INSERT INTO users (name, birthday, ssn, maiden_name)
        VALUES (?, ?, ?, ?)
    ''', (name, birthday, ssn, maiden_name))

    # Save changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # Get user input
    name = input("Enter your name: ")
    birthday = input("Enter your birthday: ")
    ssn = input("Enter your social security number: ")
    maiden_name = input("Enter your mother's maiden name: ")

    # Add user to the database
    add_user(name, birthday, ssn, maiden_name)

    print("User data added to the database.")
