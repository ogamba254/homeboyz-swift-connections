import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','bs_project.settings')
import django
django.setup()
from django.db import connection

models_to_check = []
try:
    from bookingApp.models import Route, Bus, Booking, Passenger
    models_to_check = [
        ('Route', Route),
        ('Bus', Bus),
        ('Passenger', Passenger),
        ('Booking', Booking),
    ]
except Exception as e:
    print('Could not import bookingApp.models:', e)

print('\nDatabase file:', os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db.sqlite3')))
print('Connection engine:', connection.settings_dict.get('ENGINE'))

for name, model in models_to_check:
    try:
        qs = model.objects.all()
        count = qs.count()
        print(f'\n{name} count: {count}')
        for obj in qs[:5]:
            # Generic display
            print(' -', str(obj))
    except Exception as e:
        print(f'Error querying {name}:', e)

# Also show raw table names present in SQLite
try:
    with connection.cursor() as cur:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cur.fetchall()]
    print('\nSQLite tables:', tables)
except Exception as e:
    print('Error listing SQLite tables:', e)

print('\nDone.')
