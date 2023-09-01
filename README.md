# netguru_prj_2
To run app:
- go to root of project:
1. create .env file with this structure:
DEBUG=1
SECRET_KEY=dummy
DJANGO_ALLOWED_HOSTS=localhost 0.0.0.0 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=dummy
SQL_USER=dummy
SQL_PASSWORD=dummy
SQL_HOST=dummy
SQL_PORT=5432
DATABASE=dummy
DELETE_KEY=X-API-KEY
DELETE_KEY_VALUE=SECRET_API_KEY
APP_PORT=1339
2. after the creating the file install docker on machine an run this command on root of project
  - docker-compose up

