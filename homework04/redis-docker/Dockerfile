FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

ENV LC_CTYPE=en_US.UTF-8
ENV LANG=en_US.UTF-8

COPY . /app
WORKDIR /app

RUN pip3 install petname==2.2
RUN pip3 install Flask-Cors requests
RUN pip3 install redis

ENTRYPOINT ["python3"]
CMD ["app.py"]