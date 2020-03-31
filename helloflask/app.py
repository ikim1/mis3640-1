from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    if name:
        return render_template('hello.html', name=name)
    else:
        return '<h1>Hello, world!</h1>'


# make a route like '/double/<number>' so the webapp will return
# two times of the number

@app.route('/double/<number>')
def double(number=None):
    if number:
        result = float(number) * 2
        return f'{result}'
    else:
        return 'No number given.'