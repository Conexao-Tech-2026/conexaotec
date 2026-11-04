#Define a imagem base do contentor. Neste caso, o ambiente começará a partir da imagem oficial do Python, na sua versão 3.
FROM python:3

#Configura o diretório de trabalho principal dentro do contentor. Qualquer comandoseguinte (como o RUN ou COPY) será executado dentro desta pasta /usr/src/app.
WORKDIR /usr/src/app

#Executa este comando no terminal do contentor durante a fase de construção (build) da imagem. Serve para instalar a framework Flask através do gestor de pacotes pip.
RUN pip install flask

#Serve como documentação, informando que a aplicação dentro do contentor irá escutar ligações e pedidos na porta 5000.
EXPOSE 5000

#Copia o ficheiro app.py que está na sua máquina local (dentro da pasta ./arquivos/) para o diretório de trabalho atual do contentor (representado pelo ., que corresponde à pasta definida no WORKDIR).
COPY ./arquivos/app.py .

#Define o comando padrão que será executado automaticamente assim que o contentor for iniciado. Basicamente, chama o interpretador de Python para correr o teu ficheiro ./app.py.
CMD [ "python", "./app.py" ]
