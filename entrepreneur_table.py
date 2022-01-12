from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'
db = SQLAlchemy(app)
meta = db.MetaData()

entrepreneur = db.Table(
    'timber', meta,
    db.Column('Student_USN', db.String, primary_key=True),
    db.Column('Company_name', db.String),
    db.Column('Company_website', db.String),
    db.Column('Company_email', db.String)
)
meta.create_all(db.engine)

def create(body):
    conn = db.engine
    Student_USN = str(body['Student_USN'])
    Company_name = str(body['Company_name'])
    Company_website = str(body['Company_website'])
    Company_email = str(body['Company_email'])
    result = entrepreneur.insert().values({'Student_USN': Student_USN, 'Company_name': Company_name,
                                           'Company_website': Company_website, 'Company_email': Company_email})
    x = db.engine.execute(result)
    db.session.commit()

def read():
    view = entrepreneur.select()
    result = db.engine.execute(view)
    row_list = []
    for row in result.fetchall():
        row_list.append(dict(row))
    return jsonify(row_list)

def update(body):
    a = dict(body)
    usn = str(body['Student_USN'])
    for key, value in a.items():
        new = entrepreneur.update().where(
            entrepreneur.c.Student_USN == usn).values({key: value})
        result = db.engine.execute(new)

def delete(body):
    x = body['Student_USN']
    stmt = entrepreneur.delete().where(entrepreneur.c.Student_USN == x)
    result = db.engine.execute(stmt)
