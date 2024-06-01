FROM django:latest
COPY . .
ENTRYPOINT ['python3', 'manage.py', 'runserver']
