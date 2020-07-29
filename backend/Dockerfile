# use python container image
FROM python:3.6-stretch

# set the working directory of the image filesystem
WORKDIR /backend

# copy current directory to the working directory
ADD . /backend

# Install the python dependencies
RUN pip install -e .

EXPOSE 5000

# start the uWSGI
CMD ["uwsgi", "app.ini"]
