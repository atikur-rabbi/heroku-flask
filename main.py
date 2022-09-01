from flask import Flask, render_template

import os

port = int(os.environ.get('PORT', 5000))

app.run(host='0.0.0.0', port=port, debug=True)

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world !!'


@app.route('/test')
def test():
    return 'Test'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)
