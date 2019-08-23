import sqlite3

conn = sqlite3.connect('books.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

# Create table - CLIENTS
c.execute('''CREATE TABLE books
             ([id] INTEGER PRIMARY KEY,[published] text, [author] text)''')
         