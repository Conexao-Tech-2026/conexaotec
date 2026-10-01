FROM python:3

WORKDIR /usr/src/app

#COPY requirements.txt./
RUN pip install flask

COPY ./arquivos/app.py .

CMD [ "python", "./app.py" ]
