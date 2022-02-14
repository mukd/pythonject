from flask import Flask
app = Flask(__name__)
app.debug=True

#@app.route('/')
def hello():
    return 'hello,world!'

@app.route('/login')
def login():
    return 'Login'

#路由
@app.route('/')
def index():
    return 'hello,world!'
if __name__ == '__main__':
    #app.run(host='127.0.0.1',port=5000)
    app.run()
