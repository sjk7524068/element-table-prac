from flask import Flask, render_template
from  flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is my place'
socketio = SocketIO(app, cors_allowed_origins='*')


@socketio.on('message')
def handle_message(message):
    print(message)
    socketio.emit('response', message)


@socketio.on('connect', namespace='/chat')
def test_connect():
    print('连接成功！')
    socketio.emit('my response', {'data':'hello, connected !'}, namespace='/chat')


@socketio.on('message', namespace='/andy')
def handle_andy_message(message):
    print('andy', message)
    socketio.emit('response', message, namespace='andy')


@socketio.on('chat', namespace='/chat')
def chat_room(message):
    print(message)
    socketio.emit('chat', message, namespace='/chat')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8866)