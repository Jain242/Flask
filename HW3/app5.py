from flask import  Flask, render_template, request, redirect, make_response
from model1 import db, Author, Books
from forms2 import LoginForm
from random import choice,randint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')




@app.cli.command('add-user')
def add_user():

    for i in range(1, 11):
        author = Author(name=f'Имя_{i}', lastname=f'Фамилия_{i}')
        db.session.add(author)
    db.session.commit()

    for i in range(1, 21):
        author = Author.query.get(randint(1, 10))
        book = Books(name=f'Книга_{i}', years_start=randint(1800, 2022), copies=randint(1, 10), author=author)
        db.session.add(book)
    db.session.commit()


@app.route('/')
def index():
    book = Books.query.all()
    return render_template('index.html', books  = book)




if __name__ == '__main__':
    app.run(debug=True)



# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route("/login", methods=["POST"])
# def welcome():
#     if request.method == "POST":
#         name = request.form.get('name')
#         email = request.form.get('email')
#         response = make_response(redirect('/greet'))
#         response.set_cookie('username', name)
#         return response
    
# @app.route('/greet')
# def greet():
#     username = request.cookies.get('username')
#     return render_template('login.html', username=username)


# @app.route('/logout')
# def logout():
#     response = make_response(redirect('/'))
#     response.set_cookie('username', '', expires=0)
#     return response
