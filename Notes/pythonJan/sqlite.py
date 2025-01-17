import sqlite3

conn = sqlite3.connect("example.db") # connection
c = conn.cursor() # cursor

# commands
# CREATE - create table
# INSERT - inserting data into table
# SELECT - query data
# UPDATE - modifying data
# DELETE - deleting
# WHERE - filtering

# Create a database

c.execute("""
    CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT )
"""
)

conn.commit() # save the change

#insert data
# ? - placeholders
# safe to use

c.execute("""
    INSERT INTO students (name, age, grade)
    VALUES (?, ?, ?)          
""", ("Andrew", 30, "B"))

conn.commit()

# update

c.execute("""
    UPDATE students
    SET grade = ?
    WHERE name = ?
""", ("A", "Andrew"))
conn.commit()

# query

c.execute("SELECT * FROM students")
conn.commit()

x = c.fetchall()

for data in x:
    print(data)
    
# DELETE
c.execute("""
    DELETE FROM students
    WHERE name = ?
""", ("Andrew",))

conn.commit()

x = c.fetchall()

for data in x:
    print(data)
    