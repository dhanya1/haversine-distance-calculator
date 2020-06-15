FROM python:3.6-slim
EXPOSE 8000:8000
WORKDIR /intercom
COPY . /intercom
RUN pip install -r requirements.txt
CMD ["gunicorn","-c","gunicorn_conf.py", "wsgi", "--reload"]