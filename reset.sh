rm -f db.sqlite3
python manage.py migrate
echo 'from django.contrib.auth.models import User; User.objects.create_superuser(username="'${LIMS_DEVEL_ADMIN_USERNAME}'", password="'${LIMS_DEVEL_ADMIN_PASSWORD}'", email="'${LIMS_DEVEL_ADMIN_EMAIL}'")' | python manage.py shell