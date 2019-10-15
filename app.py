# this is really only meant to be used by openshift; duplicates reset.sh

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lims.settings')
import django
django.setup()
from lims import settings
import shutil
shutil.rmtree(os.path.join(settings.BASE_DIR, 'lims', 'migrations'), ignore_errors=True)
from django.core.management import call_command
call_command('migrate', no_input=True)
call_command('makemigrations', 'lims')
call_command('migrate', no_input=True)
from django.contrib.auth.models import User
u = User.objects.get(username='admin')
u.set_password('password')
u.email = 'njbooher@iastate.edu'
u.is_superuser = True
u.is_staff = True
u.save()
call_command('runserver', '0.0.0.0:8080')