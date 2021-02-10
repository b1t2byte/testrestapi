FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /src
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
COPY . /src/
EXPOSE 8000
CMD ["python","manage.py","migrate"]
CMD ["python","manage.py","runserver", "0.0.0.0:8000"]
