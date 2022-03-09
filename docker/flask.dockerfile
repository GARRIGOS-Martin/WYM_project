FROM python:3.9.10

LABEL maintainer="martin.garrigos38@gmail.com"
 

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]