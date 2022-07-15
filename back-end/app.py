from flask import Flask, request, jsonify
from flask_migrate import Migrate

from utils.database import db, DbProfiles, DbTables

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


def check_parsed_data(data):
    if not data:
        # TODO: Add logging
        return jsonify({'status': 400, 'message': 'No data provided'}), 400
    return data


@app.route('/')
def index():
    return 'hi'


@app.route('/database/add', methods=['POST'])
def create_db_profile():
    data: dict = request.get_json()
    data: (tuple, dict) = check_parsed_data(data)

    if isinstance(data, tuple):
        return data

    if data.get('name') is None:
        return jsonify({'status': 400, 'message': 'No database name provided'}), 400

    if data.get('username') is None:
        return jsonify({'status': 400, 'message': 'No database username provided'}), 400

    if data.get('password') is None:
        return jsonify({'status': 400, 'message': 'No database password provided'}), 400

    if data.get('host') is None:
        return jsonify({'status': 400, 'message': 'No database host provided'}), 400

    if data.get('port') is None:
        return jsonify({'status': 400, 'message': 'No database port provided'}), 400

    if data.get('database') is None:
        return jsonify({'status': 400, 'message': 'No database name provided'}), 400

    if data.get('type') is None:
        return jsonify({'status': 400, 'message': 'No database type provided'}), 400

    if data.get('type') not in ['mysql', 'postgresql']:
        return jsonify({'status': 400, 'message': 'Invalid database type provided'}), 400

    db_data = DbProfiles(
        name=data.get('name'), username=data.get('username'), password=data.get('password'),
        host=data.get('host'), port=data.get('port'), database=data.get('database'), type=data.get('type')
    )

    db.session.add(db_data)
    db.session.commit()

    return jsonify({'status': 201, 'message': 'Database profile created'}), 201


@app.route('/database/list', methods=['GET'])
def list_db_profiles():
    db_profiles = DbProfiles.query.all()

    if not db_profiles:
        return jsonify({'status': 404, 'message': 'No database profiles found'}), 404

    data = []
    for db_profile in db_profiles:
        data.append({
            'id': db_profile.id,
            'name': db_profile.name,
        })

    return jsonify({'status': 200, 'message': 'Database profiles listed', 'data': data}), 200


@app.route('/database/<int:db_profile_id>/tables', methods=['GET'])
def get_database_tables(db_profile_id):
    db_tables = DbTables.query.filter_by(id=db_profile_id).all()

    if not db_tables:
        return jsonify({'status': 404, 'message': 'No database tables found'}), 404

    data = []
    for db_table in db_tables:
        data.append({
            'id': db_table.id,
            'name': db_table.name,
        })

    return jsonify({'status': 200, 'message': 'Database tables listed', 'data': data}), 200


if __name__ == '__main__':
    app.run()
