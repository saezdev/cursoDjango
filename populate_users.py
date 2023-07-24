import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

##FAKE POPULATION SCRIPT
import random
from first_app.models import Users
from faker import Faker
from django.db import IntegrityError

fakegen = Faker()


def populate(N=5):
    
    #Borramos todos los usuarios existentes antes de añadir nuevos
    Users.objects.all().delete()
    
    for entry in range(N):
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()
        
        #Crear usuarios apartir del indice 0 y rellenarlos con datos ficticios
        try:
            users = Users.objects.get_or_create(f_name=fake_fname, l_name=fake_lname, email=fake_email)
        except IntegrityError:
            print('Duplicated encountered..')
            pass
          
        
if __name__ == '__main__':
    print('Populating script!')
    populate(20)
    print('Populating complete!')