from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! My name is Gemma'
@app.route('/date')
def date():  # put application's code here
    return render_template('date.html')

if __name__ == '__main__':
    app.run()
