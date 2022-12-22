FROM python:3.11
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN mkdir /app
WORKDIR /app
COPY rocky .
ENTRYPOINT [ "python", "manage.py", "runserver", "0:8000"]
