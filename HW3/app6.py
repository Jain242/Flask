from flask import Flask, render_template, redirect, url_for
from forms2 import RegistrationForm
from model import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydbusers.db'
app.config['SECRET_KEY'] = '2sd827af7236a76f5a4d7asd' 
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        form.save_user()
        return redirect(url_for('success'))
    return render_template('index2.html', form=form)


@app.route('/success')
def success():
    return 'Вы успешно зарегистрированы!'

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
