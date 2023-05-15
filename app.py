from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route("/signed_up")
def signed_up():
    return render_template("signed_up.html")


if __name__ == '__main__':
    app.run(debug=True)