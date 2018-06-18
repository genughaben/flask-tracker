# use barebones image version of python 3.6.5
FROM python:3.6.5-slim
MAINTAINER Frank Wolf <fwolf@posteo.de>

# Set an environment variable to store where the app is installed to inside
# of the Docker image.
ENV INSTALL_PATH /tracker
RUN mkdir -p $INSTALL_PATH

# This sets the context of where commands will be ran in
WORKDIR $INSTALL_PATH

# Ensure requirements are cached and only get updated when they change. This will
# drastically decrease build times when your requirements do not change.
COPY requirements-docker.txt requirements-docker.txt
RUN pip install -r requirements-docker.txt

# Copy in the application code from your work station at the current directory
# over to the working directory.
COPY . .

# With pip install -e for local projects, the "SomeProject.egg-info" directory
# is created relative to the project path. This is one advantage over just using
# setup.py develop, which creates the "egg-info" directly relative the current
# working directory. More: docs
RUN pip install --editable .

# The default command that gets ran will be to start the Unicorn server.
CMD gunicorn -b 0.0.0.0:8765 --access-logfile - "tracker.app:create_app()"
