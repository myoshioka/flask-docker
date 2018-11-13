FROM python:3.6
ADD . /code
WORKDIR /code
RUN apt-get update && apt-get install -y libpq-dev postgresql-client
RUN pip install -r requirements.txt

