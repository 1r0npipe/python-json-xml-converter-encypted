FROM python:3

COPY ./getweather.py /usr/src/app/
COPY requirements.txt /usr/src/app/requirements.txt

WORKDIR /usr/src/app

RUN pip install -r requirements.txt



CMD [ "python", "./getweather.py" ]