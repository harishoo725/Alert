FROM python:latest

ADD new.py .

RUN pip install elasticsearch sendgrid

CMD [ "python", "./new.py" ]