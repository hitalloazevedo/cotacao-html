from flask import Flask, render_template
from api import getPrice

app = Flask(__name__)

@app.route("/")
def index():

    dollarPrice = getPrice('USD')
    euroPrice   = getPrice('EUR')

    return render_template('index.html', usd=dollarPrice, eur=euroPrice)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')