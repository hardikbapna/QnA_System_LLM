FROM python:3.10.9
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["gunicorn","-b","0.0.0.0:8080","app:demo"]
#CMD gunicorn --bind 0.0.0.0:7860 app:demo