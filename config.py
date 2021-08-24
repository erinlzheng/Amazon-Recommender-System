## THIS IS WHERE WE EDIT THE SETTINGS FOR THE APPLICATION
#  We can configure our database credentials here
DEGUG = True
SQL_USERNAME = "postgres" #your personal username goes here
SQL_PASSWORD = "postgres" #your personal password goes here
DB_NAME = "data_science_careers" #The default name of the DB
LOCAL_PORT = 5432
SQLALCHEMY_DATABASE_URI = f"postgresql://{SQL_USERNAME}:{SQL_PASSWORD}@localhost:{LOCAL_PORT}/{DB_NAME}"