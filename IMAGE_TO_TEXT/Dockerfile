FROM ubuntu:latest
WORKDIR /Django
COPY . .
RUN apt update -y
RUN apt upgrade -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN apt install tesseract-ocr -y
RUN pip3 install -r requerments.txt
EXPOSE 8000
CMD python3 manage.py runserver 0:8000