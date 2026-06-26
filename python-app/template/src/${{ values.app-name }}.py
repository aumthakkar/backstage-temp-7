from flask import Flask, jsonify
import socket
import time

app = Flask(__name__)

@app.route('/api/v1/info')  
def info():
    return jsonify({
        "host": socket.gethostname(),
        "time": time.ctime(),
        "env": "dev",
        "msg": "Hi Pranav! How are you?"

    })

@app.route('/api/v1/healthz')  
def healtz():
    return jsonify({
        "status": "up"

    })

if __name__ == '__main__':
    app.run("0.0.0.0")

