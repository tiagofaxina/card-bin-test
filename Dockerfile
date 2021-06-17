FROM ubuntu:20.04


RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/

RUN pip3 install -r requirements.txt
RUN pip3 install modin[all]
COPY . .
EXPOSE 5000

CMD ["python3", "./src/app.py"]


