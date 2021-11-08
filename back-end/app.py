from flask import Flask, render_template
from flask_migrate import Migrate

# Parent imports are different between windows and linux
try:
    from .utils.database import db
except ImportError:
    from utils.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
