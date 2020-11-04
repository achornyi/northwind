Training project with bundle of Django+DRF+Postgresql+Celery+Docker

DB source and configs: https://github.com/pthom/northwind_psql

For launch project, add .env file to northwind folder with all required data for DB connection 
(look northwind/northwind/settings.py).

After this, in terminal from project root run:
>$ docker-compose up

If you encounter a migration problem, open new terminal and from project root run
>$ docker-compose exec django python manage.py migrate `<appname>` 0001 --fake