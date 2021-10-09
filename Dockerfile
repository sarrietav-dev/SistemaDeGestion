FROM python:3.7-slim

RUN python -m pip install --upgrade pip

COPY requirements/production.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY  . .

ENV FLASK_APP=web/app.py

EXPOSE 5000

CMD [ "flask", "run" ]
