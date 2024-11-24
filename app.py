from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
import subprocess

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)
app.app_context().push()

class Horoscope(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sign = db.Column(db.String(20), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Horoscope %r>' % self.id

@app.route('/',)
def index():
    horoscopes = Horoscope.query.order_by(Horoscope.date.desc()).all()
    return render_template('index.html', horoscopes=horoscopes)

@app.route('/add_horoscope', methods=['POST', 'GET'])
def adder():
    if request.method == 'POST':
        sign = request.form['title']
        desc = request.form['description']

        horoscope = Horoscope(sign=sign, text=desc)

        try:
            db.session.add(horoscope)
            db.session.commit()
            return redirect('/')
        except:
            return 'При добавлении гороскопа произошла ошибка'
    else:
        return render_template('add_horoscope.html')

if __name__ == '__main__':
    app.run()