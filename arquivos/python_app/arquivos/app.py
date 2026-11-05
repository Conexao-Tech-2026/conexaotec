#Importa o framework Flask e o manipulador de pedidos.
from flask import Flask, request

#Inicializa a aplicação web
app = Flask(__name__)


#Configura a rota principal (raiz).
@app.route("/", defaults={"path": ""})

#Captura qualquer outra rota que seja acedida (catch-all).
@app.route("/<path:path>")

#Função executada sempre que as rotas acima são chamadas.
def home(path):

    #Obtém o IP real do cliente (prioriza proxies como o Nginx, mas tem o IP diret    o como plano B).
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    host = request.headers.get("Host", request.host)

    #Mostra o IP formatado na resposta.
    return f"Seu IP é: {ip}\nSeu Host é: {host}"

#Garante que o servidor só arranca se o ficheiro for executado diretamente.
if __name__ == "__main__":

    #Inicia o servidor na porta 5000, aberto a ligações externas.
    app.run(host="0.0.0.0", port=5000)
