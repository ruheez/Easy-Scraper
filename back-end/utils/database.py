from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class DbProfiles(db.Model):
    __tablename__ = 'db_profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    host = db.Column(db.String(50), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    database = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)


class DbTables(db.Model):
    __tablename__ = 'db_tables'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey('db_profiles.id'))

    profile = db.relationship('DbProfiles', backref='tables')