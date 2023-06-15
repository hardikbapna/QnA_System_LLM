FROM python:3.10.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 7860
CMD gunicorn --bind 127.0.0.1:7860 app:demo