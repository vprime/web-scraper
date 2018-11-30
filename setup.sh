apt-get update && \
	apt-get -y install python3 python-dev python3-dev \
    build-essential

pip install virtualenv
virtualenv env
./env/Scripts/activate
pip -I stable-req.txt
python3 run.py