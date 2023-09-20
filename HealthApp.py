from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['RegisteredUsers']
collection = db['users']

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def landingPage():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def loginPage():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = collection.find_one({'name': username, 'password': password});

        if user is not None:
            print("User Verified")
            return render_template('dashboard.html', username=username);
        else:
            print("User not verified")
            return render_template('login.html');

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        gender = request.form['gender']
        dob = request.form['dob']
        password = request.form['password']

        # Insert the user into the MongoDB collection
        collection.insert_one({
            'name': name,
            'email': email,
            'age': age,
            'gender': gender,
            'dob': dob,
            'password': password
        })

        return redirect(url_for('loginPage'))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'GET' or request.method == 'POST':
        return render_template('dashboard.html')
    
    


@app.route('/update')
def updateUserProfile():
    return render_template('update.html')

@app.route('/chatbot')
def chatBot():
    return render_template('chatbot.html')

if __name__ == '__main__':
    app.run(debug=True)
