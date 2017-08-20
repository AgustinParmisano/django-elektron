# djangorest-elektron

Following DjangoRest Tutorial: http://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/
Integrating with Devices Class.
Integrating postgre.

# To restart model

>rm -rf "*00*"
>rm -rf "*.pyc"

>su postgres

postgres> psql
psql> DROP DATABASE elektron;
psql> CREATE DATABASE elektron;

exit pqsl (ctrl + D)
exit user postgres (ctrl + D)

>python manage.py makemigrations
>python manage.py migrate
>python manage.py createsuperuser
