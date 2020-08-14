FROM python:3.6-stretch
WORKDIR /backend
ADD . /backend
RUN pip install -e .
CMD flask db upgrade
CMD ["uwsgi", "app.ini"]
