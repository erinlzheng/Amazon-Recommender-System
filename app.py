from flask import Flask, render_template, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, support_credentials = True)

@app.route("/index")
@app.route("/index.html")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/products")
@app.route("/products.html")
def change():
    return render_template('produts.html')


@app.route("/insights")
@app.route("/insights.html")
def insights():
    return render_template('insights.html')

@app.route("/tutorial")
@app.route("/tutorial.html")
def tutorial():
    return render_template('tutorial.html')

@app.route("/viz1")
@app.route("/viz1.html")
def viz1():
    return render_template('viz1.html')

@app.route("/viz2")
@app.route("/viz2.html")
def viz2():
    return render_template('viz2.html')

@app.route("/viz3")
@app.route("/viz3.html")
def viz3():
    return render_template('viz3.html')

@app.route('/get_top20_avg_rating', methods=['GET'])
def get_top20_avg_rating():
    file_path = "./static/data/Top_20_avg_rating_products.json"
    result = []
    with open(file_path) as f:
        for line in f:
            result.append( json.loads(line.strip("\n")) )
    return jsonify(result)

@app.route('/get_top20_rated', methods=['GET'])
def get_top20_rated():
    file_path = "./static/data/Top_20_rated_products.json"
    result = []
    with open(file_path) as f:
        for line in f:
            result.append( json.loads(line.strip("\n")) )
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
