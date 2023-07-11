FROM python:3.8

MAINTAINER Codium <info@codium.team>

WORKDIR /opt/project

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

VOLUME ["/opt/project"]
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]