from flask import  Flask, render_template, request, redirect, make_response

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route("/login", methods=["POST"])
def welcome():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        response = make_response(redirect('/greet'))
        response.set_cookie('username', name)
        return response
    
@app.route('/greet')
def greet():
    username = request.cookies.get('username')
    return render_template('login.html', username=username)


@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('username', '', expires=0)
    return response





if __name__ == '__main__':
    app.run(debug=True)
