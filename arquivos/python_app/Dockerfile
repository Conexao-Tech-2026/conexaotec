FROM python:3

WORKDIR /usr/src/app

#COPY requirements.txt./
RUN pip install flask
EXPOSE 5000
COPY ./arquivos/app.py .

CMD [ "python", "./app.py" ]
