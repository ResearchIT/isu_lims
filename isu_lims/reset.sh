rm -f db.sqlite3
rm -rf lims/migrations
python manage.py migrate
python manage.py makemigrations lims
python manage.py migrate
echo 'from django.contrib.auth.models import User; User.objects.create_superuser(username="admin", password="password", email="njbooher@iastate.edu")' | python manage.py shell