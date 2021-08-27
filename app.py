from flask import Flask, render_template, jsonify, url_for
import flask
from flask_cors import CORS
import json
import itertools
import numpy as np
from numpy.core.numeric import indices 
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
from boto.s3.connection import S3Connection
import os

app = Flask(__name__)
CORS(app, support_credentials=True)
# s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])
# s3_handler = new S3Handler(os.environ.get('S3_KEY'), os.environ.get('S3_SECRET'))

data = pd.read_csv('C:\\Users\\erinz\\Downloads\\ez boot camp\\Projects\\Project-3-Recommender-System\\static\\data\\merged.csv') 
df = data[['asin', 'user', 'rating']] 
df1= df.dropna()
new_df = df1.head(100000)
ratings_matrix = new_df.pivot_table(values='rating', index='user', columns='asin', fill_value=0)

indices = pd.Series(new_df.index, index=new_df['asin'])
all_asin = [new_df['asin'][i] for i in range(len(new_df['asin']))]

# df2 = ratings_matrix.reset_index()
# indices = pd.Series(df2.index, index=df2['asin'])
# all_asin = [df2['asin'][i] for i in range(len(df2['asin']))]

# DEF
def get_recommendations(asin):
    X = ratings_matrix.T
    X1 = X
    SVD = TruncatedSVD(n_components=10)
    decomposed_matrix = SVD.fit_transform(X)
    correlation_matrix = np.corrcoef(decomposed_matrix)
    i = asin
    product_id = list(X.index)
    asin_id = product_id.index(i)
    correlation_asin_id = correlation_matrix[asin_id]
    Recommend = list(X.index[correlation_asin_id > 0.65])
    Recommend.remove(i) 
    recommend10 = Recommend[0:10]
    return recommend10


# APP ROUTES
#@app.route("/index")
#@app.route("/index.html")
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
    if flask.request.method == 'GET':
        return(render_template('products.html'))

    if flask.request.method == 'POST':
        p_name = flask.request.form['product_name']

        if p_name not in all_asin:
            return(render_template('negative.html',name=p_name))
        else:
            result_final = get_recommendations(p_name)
            names = []
            for x in result_final:
                amazon_url = 'https://amazon-asin.com/asincheck/?product_id='+x
                names.append(amazon_url)
            return flask.render_template('positive.html',product_names=names,search_name=p_name)


            # for x in products:
            #     amazon_url = 'https://www.amazon.com/s?k='+x+'&ref=nb_sb_noss'
            #     recs = []
            #     recs.append(amazon_url)
            #     return recs

        # names = result_final
        # for i in range(len(result_final)):
        #     amazon_url = 'https://www.amazon.com/s?k='+i+'&ref=nb_sb_noss'
        #     # names.append(result_final.iloc[i][0])
    
        # return flask.render_template('positive.html',product_names=names,search_name=m_name)
        

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
    

@app.route("/detail1")
@app.route("/detail1.html")
def detail1():
    return render_template('detail1.html')


@app.route("/detail2")
@app.route("/detail2.html")
def detail2():
    return render_template('detail2.html')

@app.route("/detail3")
@app.route("/detail3.html")
def detail3():
    return render_template('detail3.html')

@app.route("/detail4")
@app.route("/detail4.html")
def detail4():
    return render_template('detail4.html')

@app.route("/detail5")
@app.route("/detail5.html")
def detail5():
    return render_template('detail5.html')

@app.route("/detail6")
@app.route("/detail6.html")
def detail6():
    return render_template('detail6.html')

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
