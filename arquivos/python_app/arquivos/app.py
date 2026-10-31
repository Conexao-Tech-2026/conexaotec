from flask import Flask, request

app = Flask(__name__)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def home(path):
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    return f"Seu IP é: {ip}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
