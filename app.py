from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_random_article')
def get_random_article():
    while True:
        a = "https://en.wikipedia.org/wiki/Special:Random"
        u = requests.get(a)
        soup = BeautifulSoup(u.content, 'html.parser')
        title = soup.find(class_="firstHeading").text.replace(' ', '_')
        return jsonify(title=title)

if __name__ == '__main__':
    app.run(debug=True)
