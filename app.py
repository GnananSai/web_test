from flask import Flask, jsonify, render_template, request
from database import load_login_info, get_pass

app = Flask(__name__)


@app.route('/')
def hello_world():
  login_info = load_login_info()
  return render_template('home.html', users=login_info)


@app.route("/login", methods=['post'])
def login():
  data = request.form
  username = data['username']
  password = data['password']
  real = get_pass(username)
  if (password == real):
    print("passwords match")
    return render_template('success.html')
  else:
    print("passwords dont match")
    return render_template('fail.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
