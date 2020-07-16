FROM python:3

COPY ./* /usr/src/app/

WORKDIR /usr/src/app

RUN pip install -r requirements.txt && pip3 install json2xml && pip3 install flask


EXPOSE 5000

CMD [ "python", "./cont_a.py" ]