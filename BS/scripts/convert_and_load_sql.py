import re
import sqlite3
import os
import sys

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SQL_PATHS = [
    os.path.join(BASE, 'db.sqlite3.sql'),
    os.path.join(BASE, 'bookingApp', 'dbsql', 'bus_booking_system.sql'),
]
SQL_FILE = None
for p in SQL_PATHS:
    if os.path.exists(p):
        SQL_FILE = p
        break

if not SQL_FILE:
    print('No SQL dump found in expected locations:', SQL_PATHS)
    sys.exit(1)

print('Using SQL file:', SQL_FILE)
with open(SQL_FILE, 'r', encoding='utf-8', errors='ignore') as f:
    sql = f.read()

# Basic cleanups to convert MySQL dump to SQLite-friendly SQL
# 1. Remove `CREATE DATABASE` / `USE` statements
sql = re.sub(r"CREATE\s+DATABASE.*?;", "", sql, flags=re.IGNORECASE | re.S)
sql = re.sub(r"USE\s+\w+\s*;", "", sql, flags=re.IGNORECASE)

# 2. Remove backticks
sql = sql.replace('`', '"')

# 3. Remove MySQL specific ENGINE/CHARSET/ROW_FORMAT clauses after close parenthesis
sql = re.sub(r"\)\s*ENGINE=.*?;", ");", sql, flags=re.IGNORECASE | re.S)

# 4. Replace AUTO_INCREMENT primary key definitions
# Examples: INT AUTO_INCREMENT PRIMARY KEY -> INTEGER PRIMARY KEY AUTOINCREMENT
sql = re.sub(r"\bINT\b\s+AUTO_INCREMENT\s+PRIMARY\s+KEY", "INTEGER PRIMARY KEY AUTOINCREMENT", sql, flags=re.IGNORECASE)
sql = re.sub(r"\bINT\b\s+AUTO_INCREMENT", "INTEGER", sql, flags=re.IGNORECASE)

# 5. Replace data types: VARCHAR(...) -> TEXT, DECIMAL(...) -> REAL, enum(...) -> TEXT
sql = re.sub(r"VARCHAR\s*\([^)]*\)", "TEXT", sql, flags=re.IGNORECASE)
sql = re.sub(r"DECIMAL\s*\([^)]*\)", "REAL", sql, flags=re.IGNORECASE)
sql = re.sub(r"ENUM\s*\([^)]*\)", "TEXT", sql, flags=re.IGNORECASE)

# 6. Replace `INT AUTO_INCREMENT` style primary keys where PRIMARY KEY appears separately
sql = re.sub(r"\bINT\b\s+PRIMARY\s+KEY", "INTEGER PRIMARY KEY", sql, flags=re.IGNORECASE)

# 7. Remove MySQL-specific `UNIQUE KEY` or `KEY` / `CONSTRAINT` index definitions placed outside CREATE TABLE (simple strategy: remove lines starting with KEY or UNIQUE KEY)
sql = '\n'.join([line for line in sql.splitlines() if not re.match(r"^\s*(KEY|UNIQUE\s+KEY|LOCK|SET|ALTER)\b", line, flags=re.IGNORECASE)])

# 8. Remove `AUTO_INCREMENT=...` and `CHARSET=...` occurrences
sql = re.sub(r"AUTO_INCREMENT\s*=\s*\d+", "", sql, flags=re.IGNORECASE)
sql = re.sub(r"DEFAULT\s+CHARSET\s*=\s*\w+", "", sql, flags=re.IGNORECASE)

# 9. Remove MySQL-specific comments like /*! ... */
sql = re.sub(r"/\*!.*?\*/;?", "", sql, flags=re.S)

# 10. Remove `ENGINE=...` that may still exist
sql = re.sub(r"ENGINE\s*=\s*\w+\s*;", ";", sql, flags=re.IGNORECASE)

# 11. Normalize semicolons and spacing
sql = re.sub(r";\s*;", ";", sql)

# Print short preview for debugging
preview = sql[:1000]
print('Preview of converted SQL (first 1000 chars):')
print(preview)

# Execute on SQLite DB
DB = os.path.join(BASE, 'db.sqlite3')
if not os.path.exists(DB):
    print('No existing db.sqlite3 found; it will be created.')

conn = sqlite3.connect(DB)
conn.execute('PRAGMA foreign_keys = ON;')
try:
    conn.executescript(sql)
    conn.commit()
    print('SQL loaded into SQLite DB successfully.')
except Exception as e:
    print('Error while executing converted SQL:', e)
    print('You may need manual fixes to the SQL dump for full compatibility.')
    conn.rollback()
    conn.close()
    sys.exit(1)

conn.close()
print('Done.')
