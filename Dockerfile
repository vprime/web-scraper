FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r stable-req.txt
ENTRYPOINT ["python"]
CMD ["run.py"]