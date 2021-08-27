DEGUG = True
SQL_USERNAME = "postgres" #your personal username goes here
SQL_PASSWORD = "postgres123" #AWS server password goes here
DB_NAME = "amazonelectronicsdb" #DB name
LOCAL_PORT = 5432
SQLALCHEMY_DATABASE_URI = f"postgresql://{SQL_USERNAME}:{SQL_PASSWORD}@amazon-electronics-db.cwwwsjftjmcz.us-east-1.rds.amazonaws.com:{LOCAL_PORT}/{DB_NAME}"