from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from entrepreneur_table import create, read, update, delete

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'
db = SQLAlchemy(app)
meta = db.MetaData()

meta.create_all(db.engine)

@app.route('/create', methods=['POST'])
def add():
    result = create(request.get_json())
    return "Inserted successfully"

@app.route('/read', methods=['GET'])
def view():
    result = read()
    return result

@app.route('/update', methods=['PUT'])
def change():
    result = update(request.get_json())
    return "Updated Successfully"

@app.route('/delete', methods=['DELETE'])
def deleting():
    result = delete(request.get_json())
    return "Deleted successfully"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
