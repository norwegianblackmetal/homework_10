FROM python:3.9
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT ["python3", "manage.py", "runserver"]