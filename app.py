from flask import Flask, render_template, jsonify
from flask_cors import CORS
import json
import numpy as np 
import pandas as pd
from sqlalchemy import create_engine
import psycopg2 as pg2
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
import sklearn.externals
import joblib
import scipy.sparse
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds
import warnings; warnings.simplefilter('ignore')
from sklearn.decomposition import TruncatedSVD

app = Flask(__name__)
CORS(app, support_credentials=True)

# DEF
def get_recommendations(asin):
    new_df = merged_df.head(5000)
    ratings_matrix = new_df.pivot_table(values='rating', index='user', columns='asin', fill_value=0)

    X = ratings_matrix.T
    X1 = X


    SVD = TruncatedSVD(n_components=10)
    decomposed_matrix = SVD.fit_transform(X)
    decomposed_matrix.shape
    correlation_matrix = np.corrcoef(decomposed_matrix)
    correlation_matrix.shape
    i = "B00004TDA2"
    product_id = list(X.index)
    asin_id = product_id.index(i)
    asin_id
    correlation_asin_id = correlation_matrix[asin_id]
    correlation_asin_id.shape
    Recommend = list(X.index[correlation_asin_id > 0.65])

    # Removes the purchased item 
    Recommend.remove(i) 
    Recommend[0:10]
    products = Recommend[0:10]
    for i in products:
        url = 'https://www.amazon.com/s?k='+i+'&ref=nb_sb_noss'
        print (url)


# APP ROUTES
@app.route("/index")
@app.route("/index.html")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
@app.route("/about.html")
def about():
    return render_template('about.html')


@app.route("/products.html", methods=['GET', 'POST'])
@app.route("/products", methods=['GET', 'POST'])
def products():
    return render_template('products.html')
def main():
    if flask.request.method == ‘GET’:
        return(flask.render_template(‘index.html’))
        
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
