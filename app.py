# this is really only meant to be used by openshift; duplicates reset.sh

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lims.settings')

import django
django.setup()

from lims import settings
import shutil
os.remove(os.path.join(settings.BASE_DIR, 'db.sqlite3'))
shutil.rmtree(os.path.join(settings.BASE_DIR, 'lims', 'migrations'), ignore_errors=True)

from django.core.management import call_command

call_command('migrate', no_input=True)
call_command('makemigrations', 'lims')
call_command('migrate', no_input=True)

from django.contrib.auth.models import User, Group, Permission

User.objects.create_superuser(username="admin", password="password", email="njbooher@iastate.edu")

from django.apps import apps
from django.contrib.contenttypes.models import ContentType

# create admin group, give it all permissions for lims app

admin_group, created = Group.objects.get_or_create(name='Admin')

for model in apps.all_models['lims']:
    content_type = ContentType.objects.get(
        app_label='lims',
        model=model
    )
    permissions = Permission.objects.filter(content_type=content_type)
    admin_group.permissions.add(*permissions)

admin_group.save()

# create standard group, give it select permissions

standard_group, created = Group.objects.get_or_create(name='Standard')

for model in apps.all_models['lims']:
    standard_group.permissions.add(Permission.objects.get(codename='view_' + model))

standard_group.permissions.add(Permission.objects.get(codename='change_project'))

for model in ['plant', 'sample', 'seed', 'seedpacket']:
    standard_group.permissions.add(Permission.objects.get(codename='add_' + model))
    standard_group.permissions.add(Permission.objects.get(codename='change_' + model))

standard_group.save()

# create user in admin group

admin_user = User.objects.create_user(username='admin_user', email='njbooher@iastate.edu', password='password12345')
admin_user.groups.set([admin_group])

# create user in standard group

standard_user = User.objects.create_user(username='standard_user', email='njbooher@iastate.edu', password='password12345')
standard_user.groups.set([standard_group])

# run dev server

call_command('runserver', '0.0.0.0:8080')