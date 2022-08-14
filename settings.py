import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()
app = Flask('app')

class app_settings():
    # user = 'postgres'
    # password = 'postgres'
    # database = 'fl_adv3'
    # user = 'app'
    # password = '1234'
    # database = 'fl_adv'
    db_name = os.environ.get('POSTGRES_DB')
    db_pass = os.environ.get('POSTGRES_PASSWORD')
    db_user = os.environ.get('POSTGRES_USER')

    app.config['SQLALCHEMY_DATABASE_URI'] =\
        f"postgresql://{db_user}:{db_pass}@127.0.0.1:5430/{db_name}"

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
    # app.config["SECRET_KEY"] = "sdf6as5df67sad54sa"
    app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')

app.config.from_object(app_settings)

