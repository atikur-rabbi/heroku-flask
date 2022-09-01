from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


@app.route('/test')
def test():
    return 'Test'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))






    
# from flask import Flask, render_template


# @app.route('/')
# def hello():
#     return 'Hello, world !!'


# @app.route('/test')
# def test():
#     return 'Test'

# @app.route('/result')
# def result():
#    dict = {'phy':50,'che':60,'maths':70}
#    return render_template('result.html', result = dict)
   
# app.run(debug=True, port=33507)
