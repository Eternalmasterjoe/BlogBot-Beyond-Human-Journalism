from flask import Flask
from flask import render_template
from generator import generate_siht

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    siht = generate_siht()
    return render_template("home.html",siht=siht)

if __name__ == "__main__":
    app.run(debug=True)
