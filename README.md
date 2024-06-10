# netguru_prj_2
To run app:
- go to root of project:
1. create .env file with this structure:
DEBUG=1
SECRET_KEY=my_secret_key
DJANGO_ALLOWED_HOSTS=localhost 0.0.0.0 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=mydatabase
SQL_USER=myuser
SQL_PASSWORD=mypassword
SQL_HOST=db
SQL_PORT=5432
DELETE_KEY=X-API-KEY
DELETE_KEY_VALUE=SECRET_API_KEY
APP_PORT=1339
2. after the creating the file install docker on machine an run this command on root of project
  - docker-compose up
3. launch app:
  http://localhost:1339 that have 2 resources :
  http://localhost:1339/dates/
  http://localhost:1339/popular/

