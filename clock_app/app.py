from flask import Flask, render_template, jsonify, request
from datetime import datetime, timedelta

app = Flask(__name__)
current_time = datetime.now()

@app.route('/')
def home():
    return render_template('index.html', time=current_time.strftime('%H:%M:%S'))

@app.route('/update_time', methods=['POST'])
def update_time():
    global current_time
    current_time -= timedelta(seconds=1)
    return jsonify({'time': current_time.strftime('%H:%M:%S')})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
