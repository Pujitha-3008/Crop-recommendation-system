from flask import Flask, request, render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
import bcrypt
import numpy as np
import joblib

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = 'secret_key'
db_sqlalchemy = SQLAlchemy(app)  

# Define SQLAlchemy User model
class User(db_sqlalchemy.Model): 
    id = db_sqlalchemy.Column(db_sqlalchemy.Integer, primary_key=True) 
    name = db_sqlalchemy.Column(db_sqlalchemy.String(100), nullable=False)
    email = db_sqlalchemy.Column(db_sqlalchemy.String(100), unique=True) 
    password = db_sqlalchemy.Column(db_sqlalchemy.String(100)) 

    def __init__(self, email, password, name):
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.name = name
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

# Create database tables
with app.app_context():
    db_sqlalchemy.create_all()

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        new_user = User(email=email, password=password, name=name)
        db_sqlalchemy.session.add(new_user)
        db_sqlalchemy.session.commit()  
        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/index1')
        else:
            return render_template('login.html', error='Invalid user')

    return render_template('login.html')

@app.route('/index1')
def index1():
    return render_template('index1.html')

@app.route("/predict", methods=['POST'])
def predict():
    N = float(request.form['Nitrogen'])
    P = float(request.form['Phosporus'])
    K = float(request.form['Potassium'])
    temp = float(request.form['Temperature'])
    humidity = float(request.form['Humidity'])
    ph = float(request.form['Ph'])
    rainfall = float(request.form['Rainfall'])

    values = [N, P, K, temp, humidity, ph, rainfall]
    if 0 < ph <= 14 and 0 <= temp < 100 and humidity > 0:
        try:
            model = joblib.load(open('crop_app', 'rb'))
        except UnicodeDecodeError as e:
            return render_template('index1.html', result='Error loading model: {}'.format(e))

        arr = [values]
        acc = model.predict(arr)

        return render_template('index1.html', result=str(acc))
    else:
        result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
        return render_template('index1.html', result=result)

def home():
    return render_template('index.html')

client = MongoClient('mongodb://localhost:27017/')
db_mongodb = client['UserDataDB']  
collection = db_mongodb['contacts']

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        Name = request.form['name']
        Phone = request.form['phone']
        Message = request.form['message']
        db_mongodb.contacts.insert_one({'name': Name, 'phone': Phone, 'message': Message})  
        return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
