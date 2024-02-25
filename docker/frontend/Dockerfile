# Use an officail Ubuntu base image 
FROM ubuntu:22.04

# Install Python and pip 
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Install app requirements 
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get install -y python3 libpq-dev git python3-dev libpq-dev
RUN python3 -m pip install urllib3 flask Flask-login kubernetes
# RUN pipenv install flask requirements Flask-login oauthlib

COPY ../../app /app/
# WORKDIR /app

#Install and needed dependencies specified in init.py 
# RUN pip3 install --no-cache-dir -r init.py
# RUN pipenv shell
# RUN ./env_prep.sh

# Set directory for running app
WORKDIR /app/frontend/src

# Start App
ENV FLASK_ENV=development
ENV FLASK_APP='.'
# RUN flask run --host=0.0.0.0 --port=3001

COPY docker/frontend/entrypoint.sh /app/frontend/src

ENTRYPOINT ["./entrypoint.sh"]
