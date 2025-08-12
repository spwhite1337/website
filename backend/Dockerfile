FROM python:3.12
WORKDIR /backend
ADD . /backend
RUN pip install -e .
CMD ["uwsgi", "app.ini"]
