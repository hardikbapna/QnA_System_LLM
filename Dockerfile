FROM python:3.10.9
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 7860
#CMD ["gunicorn","-b","0.0.0.0:$PORT","app:demo"]
#CMD gunicorn --bind 0.0.0.0:7860 app:demo
CMD waitress-serve --listen=*:7860 app:demo