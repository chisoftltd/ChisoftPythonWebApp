class app(object):
    """description of class"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')

def home():

    return "Welcome home python lovers! "

if __name__ == '__main__':
    app.run('localhost', 5050)


