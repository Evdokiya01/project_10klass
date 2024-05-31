from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

USER = "Dunya"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/account')
def account():
    return render_template("account.html")


@app.route('/course')
def course():
    return render_template("course.html")


@app.route('/forum')
def forum():
    f = open('Forum_(question).txt', 'r')
    f.readline()
    return render_template("forum.html", file=f)


@app.route('/forum_chat')
def forum_chat():
    return render_template("forum_chat.html")


@app.route('/courses')
def courses():
    f = open('Courses.txt', 'r')
    f.readline()
    return render_template("courses.html", file=f)


@app.route('/market')
def market():
    f = open('Products.txt', 'r')
    f.readline()
    return render_template("markettwo.html", file=f)


@app.route('/market_tipo')
def market_tipo():
    return render_template("market.html")


@app.route('/product')
def product():
    return render_template("product.html")


@app.route('/profile', methods=['POST', 'GET'])
def profile():
    return render_template("profile.html")


@app.route('/Registration_Profile')
def Registration_Profile():
    return render_template("Registration_Profile.html")


@app.route('/log_In_profile', methods=['POST', 'GET'])
def log_In_profile():
    if request.method == "POST":  # добавление данных
        # print(1)
        email = request.form['email']
        password = request.form['password']
        USER = email
        # print(email, password)
        try:
            # print(3)
            return redirect('/log_In_profile')
        except:
            # print(2)
            return "Неверное имя пользователя или пароль"
    else:
        return render_template("log_In_profile.html")


# @app.route('/user/<string:name>/<int:id>')
# def user(name, id):
#     return "User: " + name + " - " + str(id)


if __name__ == "__main__":
    app.run(debug=True)