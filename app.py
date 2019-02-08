import os
from os.path import join, dirname
from api import create_app

dotenv_path = join(dirname(__file__) + "/../", '.env')
if os.path.isfile(dotenv_path):
    load_dotenv(dotenv_path, verbose=True)

app = create_app({
    'SECRET_KEY': 'secret',
    'OAUTH2_REFRESH_TOKEN_GENERATOR': True,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SQLALCHEMY_DATABASE_URI': os.environ['DATABASE_URL']
})


@app.cli.command()
def initdb():
    from api.models import db
    db.create_all()
