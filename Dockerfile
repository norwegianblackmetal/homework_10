FROM python:3.9
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "manage.py", "runserver"]