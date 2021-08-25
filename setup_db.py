## IMPORTING FILES AND CONNECTING DATAFRAMES

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


# import DB config variables
from db_config import *
# Required Files
electronics_ratings = "static/data/merged.csv"
# Create DataFrames
electronics_df = pd.read_csv(electronics_ratings)
#connect to database
def execute_sql_statement(sqltext):
    conn=pg2.connect( host="localhost", database=DB_NAME, user=SQL_USERNAME, password=SQL_PASSWORD)
#cursor is an object to put watever you want
    cursor=conn.cursor()
#xecute() method
    cursor.execute(sqltext)
    conn.commit()
#Closing the connection
    conn.close()
#from config import sqldb_connect
#engine = create_engine(sqldb_connect)
#Dropping all tables gathered 
execute_sql_statement("DROP TABLE IF EXISTS merged_data CASCADE;")

#database tables
#Creating table as per requirement 
sql ='''CREATE TABLE merged_data( id INT GENERATED ALWAYS AS IDENTITY, name VARCHAR(255) NOT NULL, PRIMARY KEY(id))''' 
execute_sql_statement(sql)
print("Table created successfully........") 
#Closing the connection conn.close()

#Insert Data
#Create Engine and connection to Database
engine = create_engine(f'postgresql://{SQL_USERNAME}:{SQL_PASSWORD}@localhost:{LOCAL_PORT}/{DB_NAME}')

electronics_df.to_sql("merged_df",engine,if_exists="replace")


