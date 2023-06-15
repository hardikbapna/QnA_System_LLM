FROM python:3.10.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 7860
CMD gunicorn --workers=4 --bind 0.0.0.0:7860 app:demo