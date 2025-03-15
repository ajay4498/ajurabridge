from flask import Flask, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def home():
    return "Ajura Flask Server Running!"

@socketio.on('message')
def handle_message(msg):
    print("Received:", msg)
    socketio.send(f"Ajura Reply: {msg}")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
