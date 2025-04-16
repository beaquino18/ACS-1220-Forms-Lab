import sqlite3

# Connect to the database
conn = sqlite3.connect('books_app/database.db')
cursor = conn.cursor()

# Add the new column to the author table
try:
    cursor.execute('ALTER TABLE author ADD COLUMN date_of_birth DATE')
    print("Successfully added date_of_birth column to author table")
    conn.commit()
except sqlite3.OperationalError as e:
    print(f"Error: {e}")
    # If column already exists or other error
    conn.rollback()

# Close the connection
conn.close()
