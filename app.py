from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
socketio = SocketIO(app, async_mode='eventlet')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('get_subtitles')
def handle_get_subtitles():


    while True:
        # 1秒ごとに字幕データを送信
        with open('subtitles.json', 'r') as f:
            subtitle_data = json.load(f)        
        socketio.sleep(1)
        emit('subtitle', subtitle_data)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
