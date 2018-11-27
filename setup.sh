apt-get update && \
	apt-get -y install python3 python-dev python3-dev \
    build-essential \
	python-pip

pip install virtualenv
virtualenv env
./env/Scripts/activate
pip -I stable-req.txt
export FLASK_APP=run.py
flask run