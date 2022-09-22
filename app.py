from flask import Flask, render_template
from cotacao import pegar_cotacao


app = Flask(__name__)


@app.route("/index")
def index():

    usd = pegar_cotacao('usd')
    eur = pegar_cotacao('eur')

    return render_template('index.html', usd=usd, eur=eur)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')