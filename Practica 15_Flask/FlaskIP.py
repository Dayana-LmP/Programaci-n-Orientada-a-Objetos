#Práctica 15: Flask
#Flask con dirección IP, abre una página la cual tiene el siguiente mensaje: "You don't have the permission to access the requested resource. 
# It is either read-protected or not readable by the server."

from flask import Flask, request, abort

app = Flask(__name__)

ALLOWED_IP = '192.168.1.100'

@app.before_request
def limit_remote_addr():
    if request.remote_addr != ALLOWED_IP:
        abort(403) 
@app.route('/')
def hello_world():
    return "Hola Mundo"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)