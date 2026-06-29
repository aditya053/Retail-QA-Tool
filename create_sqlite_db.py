import sqlite3
from pathlib import Path

SQL_FILE = Path("database/retail_dataset.sql")
DB_FILE = Path("database/retail.db")

# Create the database file automatically
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

with open(SQL_FILE, "r", encoding="utf-8") as f:
    sql_script = f.read()

cursor.executescript(sql_script)

conn.commit()
conn.close()

print(f"SQLite database created successfully: {DB_FILE}")