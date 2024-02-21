# Setting up Dev Environment

* sudo apt update -y
* sudo apt install software-properties-common -y
* sudo add-apt-repository ppa:deadsnakes/ppa -y
* sudo apt install python3.7 -y
* sudo apt install libpq-dev -y
* sudo apt install git -y
* sudo apt install pipenv -y
* sudo apt install python3-dev libpq-dev From the ticketlab-frontend directory
* pipenv --python=$(which python3.8) install flask requests Flask-login oauthlib
* export FLASK_ENV=development
* export FLASK_APP='.'

# Running App
* from root director run 'pipenv shell'
* from /app run '. ./env_prep.sh'
* make sure you're in app/frontend/src directory
* flask run --host=0.0.0.0 --port=3001