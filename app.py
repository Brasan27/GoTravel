from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/gps')
def gps():
    return render_template('gps.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/lugares')
def lugares():
    return render_template('lugares.html')

if __name__ == '__main__':
    app.run(debug=True)
