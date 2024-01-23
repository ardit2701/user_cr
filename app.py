from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db = mysql.connector.connect(
    host="your_mysql_host",
    user="your_mysql_user",
    password="your_mysql_password",
    database="your_mysql_database"
)

cursor = db.cursor()

# Create users table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
    )
""")
db.commit()

# Route to display all users
@app.route('/')
def read_all_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('read_all.html', users=users)

# Route to display the form to create a new user
@app.route('/create')
def create_user_form():
    return render_template('create.html')

# Route to handle form submission and insert a new user
@app.route('/create', methods=['POST'])
def create_user():
    username = request.form['username']
    email = request.form['email']

    # Insert new user into the database
    cursor.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (username, email))
    db.commit()

    # Redirect to the Read (All) page
    return redirect('/')
# MySQL Configuration
db = mysql.connector.connect(
    host="your_mysql_host",
    user="your_mysql_user",
    password="your_mysql_password",
    database="your_mysql_database"
)

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",  # Replace with your MySQL server host
    user="your_username",  # Replace with your MySQL username
    password="your_password",  # Replace with your MySQL password
    database="your_database"  # Replace with your MySQL database name
)

if __name__ == '__main__':
    app.run(debug=True)