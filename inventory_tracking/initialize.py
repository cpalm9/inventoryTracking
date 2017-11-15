from datetime import datetime
import os
# initialize the django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'inventory_tracking.settings'
import django
django.setup()
from homepage import models as prod
from django.core import management
from django.db import connection
from datetime import datetime
import os, os.path, sys

# ensure the user really wants to do this
areyousure = input('''
  You are about to drop and recreate the entire database.
  All data are about to be deleted.  Use of this script
  may cause itching, vertigo, dizziness, tingling in
  extremities, loss of balance or coordination, slurred
  speech, temporary zoobie syndrome, longer lines at the
  testing center, changed passwords in Learning Suite, or
  uncertainty about whether to call your professor
  'Brother' or 'Doctor'.
  Please type 'yes' to confirm the data destruction: ''')
if areyousure.lower() != 'yes':
    print()
    print('  Wise choice.')
    sys.exit(1)

# drop and recreate the database tables
print()
print('Living on the edge!  Dropping the current database tables.')
with connection.cursor() as cursor:
    cursor.execute("DROP SCHEMA public CASCADE")
    cursor.execute("CREATE SCHEMA public")
    cursor.execute("GRANT ALL ON SCHEMA public TO postgres")
    cursor.execute("GRANT ALL ON SCHEMA public TO public")

# make the migrations and migrate
management.call_command('makemigrations')
management.call_command('migrate')

p1 = prod.Product()
p1.manufacturer = 'Test'
p1.man_notes = 'THIS IS A TEST'
p1.description = 'THIS IS A TEST'
p1.man_part_number = '33333'

l1 = prod.Location()
l1.city = "Provo"
l1.state = 'Utah'
l1.country = 'USA'
l1.zipcode = 84602
l1.save()
p1.location = l1
p1.save()
