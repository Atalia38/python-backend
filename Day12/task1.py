import sqlite3

# Connect to SQLite database (it creates a new database if it doesn't exist)
conn = sqlite3.connect('student_database1.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

# Function to insert a student into the database
def insert_student(name, age):
    cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

# # Function to fetch all students
def fetch_all_students():
    conn = sqlite3.connect('student_database1.db')
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
    ''')
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

# Function to update student information
def update_student(student_id, new_name, new_age):
    cursor.execute(f"UPDATE students SET name = ?, age = ? WHERE id = ?", (new_name, new_age, student_id))
    conn.commit()
    
# Function to get a student by ID
def get_student_by_id(student_id):
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    return cursor.fetchone()  # Fetch one record

# Function to delete a student
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()

# Inserting some students
insert_student('Alice', 20)
insert_student('Bob', 22)

# Fetching all students
students = fetch_all_students()
print("Students in the database:", students)

# Updating a student's data
update_student(1, 'Alice Johnson', 21)

# Fetching updated students
students = fetch_all_students()
print("Updated students in the database:", students)

# Deleting a student
delete_student(2)

# Fetching students after deletion
students = fetch_all_students()
print("Students after deletion:", students)

print(get_student_by_id(1))
# Close the connection
conn.close()

