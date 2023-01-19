FROM python:3.8
RUN mkdir -p /home/powermetter
WORKDIR /home/powermetter
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install -U pip
COPY . /home/powermetter
RUN pip install -r requirements.txt

STOPSIGNAL SIGTERM
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
