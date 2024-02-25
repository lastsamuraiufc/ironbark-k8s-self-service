# Use an officail python base image 
FROM python:3.8-slim-buster

# Set the working directory in the container 
WORKDIR /app

# Install requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# RUN apt update
RUN apt-get update

# Copy the working directory contents in the container 
COPY app/frontend/src .

# Start App
ARG app_version
ENV APP_VERSION=$app_version
ENV FLASK_APP="."
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
