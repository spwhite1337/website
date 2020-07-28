# use python container image
FROM python:3.6-stretch

# set the working directory of the image filesystem
WORKDIR /backend

# copy current directory to the working directory
ADD . /backend

# Install the python dependencies
RUN pip install -e .
RUN pip install git+https://github.com/spwhite1337/card-classifier.git
RUN pip install git+https://github.com/spwhite1337/sports-bettors.git
RUN pip install git+https://github.com/spwhite1337/presidents-speeches.git

# start the uWSGI
CMD ["uwsgi", "run.ini"]