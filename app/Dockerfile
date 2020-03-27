FROM python:3.7

COPY . .

RUN pip install -r requirements.txt
CMD python manage.py db migrate && python manage.py db upgrade