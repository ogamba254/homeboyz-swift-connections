import os, shutil, sqlite3, sys
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DB = os.path.join(BASE, 'db.sqlite3')
SQL_DUMP = os.path.join(BASE, 'bookingApp', 'dbsql', 'bus_booking_system.sql')

if not os.path.exists(SQL_DUMP):
    print('SQL dump not found:', SQL_DUMP)
    sys.exit(1)

if os.path.exists(DB):
    bak = DB + '.bak'
    print('Backing up existing DB to', bak)
    shutil.copy2(DB, bak)
    try:
        os.remove(DB)
    except Exception as e:
        print('Could not remove current DB:', e)
        sys.exit(1)

print('Creating new SQLite DB and loading SQL dump...')
conn = sqlite3.connect(DB)
with open(SQL_DUMP, 'r', encoding='utf-8') as f:
    sql = f.read()
try:
    conn.executescript(sql)
    conn.commit()
    print('Database restored successfully from', SQL_DUMP)
except Exception as e:
    print('Error while executing SQL dump:', e)
    conn.close()
    # restore backup
    if os.path.exists(DB + '.bak'):
        print('Restoring backup...')
        shutil.copy2(DB + '.bak', DB)
    sys.exit(1)
conn.close()
print('Done.')
