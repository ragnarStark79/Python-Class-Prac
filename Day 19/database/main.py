import sqlite3


# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
# cursor: A cursor is an object that allows you to execute SQL commands and retrieve results from the database. It acts as a control structure that enables traversal over the records in a database. You can use a cursor to execute SQL statements, fetch data, and manage the context of a fetch operation.
cursor = conn.cursor()


# Create a new table called 'users'
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    age INTEGER NOT NULL
)''')


# Insert some data into the 'users' table
cursor.execute('INSERT OR IGNORE INTO users (name, age) VALUES (?, ?)', ('Alice', 30))
cursor.execute('INSERT OR IGNORE INTO users (name, age) VALUES (?, ?)', ('Bob', 25))
cursor.execute('INSERT OR IGNORE INTO users (name, age) VALUES (?, ?)', ('Charlie', 35))


# Commit the changes to the database
conn.commit()

# Query the 'users' table and print the results
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
print("\nAll users:")
for row in rows:
    print(row)
    
# parameterized query to prevent SQL injection
name_to_search = 'Alice'
cursor.execute('SELECT * FROM users WHERE name = ?', (name_to_search,))
result = cursor.fetchone()
print("\nParameterized query result:")
print(result)

# second parameterized query to update a user's age
new_age = 31
cursor.execute('UPDATE users SET age = ? WHERE name = ?', (new_age, name_to_search))
conn.commit()
print(f"\nUpdated {name_to_search}'s age to {new_age}.")

# multiple sql queries in a single execution
cursor.executescript('''
INSERT OR IGNORE INTO users (name, age) VALUES ('David', 28);
INSERT OR IGNORE INTO users (name, age) VALUES ('Eve', 22);
''')

# Query the 'users' table again to see the new entries
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
print("\nAll users after inserting David and Eve:")
for row in rows:
    print(row)
    
# Close the database connection
conn.close()