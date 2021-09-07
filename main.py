from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
import requests
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    year = datetime.today().year

    return render_template('index.html', current_year=year)


if __name__ == "__main__":
    app.run(debug=True)
