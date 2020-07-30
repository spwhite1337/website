FROM python:3.6-stretch
WORKDIR /backend
ADD . /backend
RUN pip install -e .
CMD ["uwsgi", "app.ini"]
