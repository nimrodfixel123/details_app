
import os
import re
from flask import Flask, render_template, redirect, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import Email, DataRequired
from flask_wtf import FlaskForm
from sqlalchemy import text 

dbuser = os.getenv('POSTGRES_USER')
dbpass = os.getenv('POSTGRES_PASSWORD')
dbhost = os.getenv('DBHOST')
dbname = os.getenv('DBNAME')
skey = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = skey
if os.getenv('TEST_DB'):
    app.config['SECRET_KEY'] = 'sMAcUgw@*1J038*^UO3Fkpy4%Wil3M'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'  
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Contacts(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Contact {self.email}>'

class ConnectionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ConnectionForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data

        new_contact = Contacts(name=name, email=email)
        try:
            db.session.add(new_contact)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            db.session.rollback()
            return render_template('index.html', form=form, contacts=Contacts.query.all(), error=str(e)), 400
         
    contacts = Contacts.query.all()
    return render_template('index.html', form=form, contacts=contacts)

@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    contact = db.session.get(Contacts, id)
    if not contact:
        return jsonify({"error": "Contact not found"}), 404

    data = request.get_json()
    contact.name = data.get('name', contact.name)
    contact.email = data.get('email', contact.email)

    try:
        db.session.commit()
        return jsonify({"message": "Contact updated"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = db.session.get(Contacts, id)
    if contact is None:
        return jsonify({"error": "Contact not found"}), 404
    
    try:
        db.session.delete(contact)
        db.session.commit()
        return jsonify({"message": "Contact deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Error deleting contact {id}: {str(e)}")
        return jsonify({"error": "An error occurred while deleting the contact", "details": str(e)}), 400


db_initialized = False

@app.before_request
def initialize_db():
    global db_initialized
    if not db_initialized:
        db.create_all()
        db_initialized = True


@app.route('/api/health_check', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the application is up and connected to the database.
    """
    try:
        db.session.execute(text('SELECT 1'))  
        return jsonify({'status': 'OK', 'message': 'Connected to the database'}), 200
    except Exception as e:
        return jsonify({'status': 'ERROR', 'message': str(e)}), 500

