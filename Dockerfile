FROM ubuntu
ADD requirments.txt /app/
WORKDIR /app
RUN apt-get update
RUN apt install python3-pip -y
RUN pip3 install -r requirments.txt
RUN apt install ffmpeg -y 
ADD . /app
CMD ["python3","service.py"]