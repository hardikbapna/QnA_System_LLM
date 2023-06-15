FROM python:3.10.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80
CMD gunicorn --workers=4 --bind 0.0.0.0:80 app:demo