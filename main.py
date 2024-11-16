from flask import Flask, render_template, request, redirect, url_for
import threading
from bot import bot  # Импортируем вашего бота

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_bot', methods=['POST'])
def start_bot():
    # Здесь вы можете добавить логику для запуска бота или управления им
    return redirect(url_for('index'))

if __name__ == '__main__':
    threading.Thread(target=bot.polling, kwargs={'none_stop': True}).start()
    app.run(debug=True)