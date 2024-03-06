from flask import Flask, render_template

app = Flask(__name__)


products = {
    'Одежда': {'Футболки':['1000 p','фиолетовая'],
               'Брюки':['1300 p','чёрная'],
               'Платье':['1200 p','синее']},
    'Обувь': {'Кроссовки':['3500 p','белые'],
              'Туфли': ['4000 p','коричневые'],
              'Сапоги':['5000 p','черные']},
    'Куртки': {'Кожанная':['3000 p','черная'],
              'Демисезонная': ['4000 p','фиолетовая'],
              'Летняя':['2000 p','фиолетовая']},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/closes/')
def closes():
    return render_template('closes.html', products=products.get('Одежда'))

@app.route('/foot/')
def foot():
    return render_template('foot.html', products=products.get('Обувь'))

@app.route('/jacket/')
def jacket():
    return render_template('jacket.html', products=products.get('Куртки'))

if __name__ == '__main__':
    app.run(debug=True)
