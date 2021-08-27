## IMPORTING FILES AND CONNECTING DATAFRAMES
​
# import 3rd party dependencies
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
​
from db_config import *
​
# Required Files
electronics_ratings = "static/data/merged.csv"
​
# Create DataFrames
electronics_df = pd.read_csv(electronics_ratings)
​
​
#connect to database
def execute_sql_statement(sqltext):
    conn=pg2.connect( host="amazon-electronics-db.cwwwsjftjmcz.us-east-1.rds.amazonaws.com", database=DB_NAME, user=SQL_USERNAME, password=SQL_PASSWORD)
#cursor is an object to put watever you want
    cursor=conn.cursor()
#xecute() method
    cursor.execute(sqltext)
    conn.commit()
#Closing the connection
    conn.close()
​
#from config import sqldb_connect
#engine = create_engine(sqldb_connect)
​
​
#Dropping all tables gathered 
execute_sql_statement("DROP TABLE IF EXISTS merged_data CASCADE;")
​
#database tables
#Creating table as per requirement 
sql ='''CREATE TABLE merged_data( id INT GENERATED ALWAYS AS IDENTITY, name VARCHAR(255) NOT NULL, PRIMARY KEY(id))''' 
execute_sql_statement(sql)
print("Table created successfully........") 
#Closing the connection conn.close()
​
​
#Insert Data
#Create Engine and connection to Database
engine = create_engine(f'postgresql://{SQL_USERNAME}:{SQL_PASSWORD}@amazon-electronics-db.cwwwsjftjmcz.us-east-1.rds.amazonaws.com:{LOCAL_PORT}/{DB_NAME}')
​
electronics_df.to_sql("merged_df",engine,if_exists="replace")
​
#JUPYTER recommender-system-with-links
​
data = pd.read_csv(electronics_ratings) 
data.head()
​
df = data[['asin', 'user', 'rating']] 
df.head()
​
df1= df.dropna()
df1.head()
​
#Check for missing values
print('Number of missing values across columns: \n',df1.isnull().sum())
​
#Analysis of rating given by the user 
rated_per_user = df1.groupby(by='user')['rating'].count().sort_values(ascending=False)
rated_per_user.head()
​
quantiles = rated_per_user.quantile(np.arange(0,1.01,0.01), interpolation='higher')
​
new_df = df1.head(5000)
ratings_matrix = new_df.pivot_table(values='rating', index='user', columns='asin', fill_value=0)
ratings_matrix.head(50)
​
X = ratings_matrix.T
X.head()
​
from sklearn.decomposition import TruncatedSVD
SVD = TruncatedSVD(n_components=10)
decomposed_matrix = SVD.fit_transform(X)
decomposed_matrix.shape
​
correlation_matrix = np.corrcoef(decomposed_matrix)
correlation_matrix.shape
​
i = "B00004TDA2"
​
product_id = list(X.index)
asin_id = product_id.index(i)
asin_id
​
correlation_asin_id = correlation_matrix[asin_id]
correlation_asin_id.shape
​
Recommend = list(X.index[correlation_asin_id > 0.65])
​
# Removes the purchased item 
Recommend.remove(i) 
​
Recommend[0:10]
​
products = Recommend[0:10]
​
​
for i in products:
    url = 'https://www.amazon.com/s?k='+i+'&ref=nb_sb_noss'
    print (url)
​
