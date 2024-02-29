from flask import Flask, render_template, request, redirect, url_for
import bcrypt

app = Flask(__name__)

# Define the username and password
admin_username = "admin"
admin_password = "5201314".encode('utf-8')
hashed_password = bcrypt.hashpw(admin_password, bcrypt.gensalt())

@app.route('/adminlog.html')
def admin_login():
    return render_template('adminlog.html')

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the form
    username = request.form['username']
    password = request.form['password'].encode('utf-8')

    # Check if the username and password match
    if username == admin_username and bcrypt.checkpw(password, hashed_password):
        # Password is correct, redirect to admin page
        return redirect(url_for('flag'))
    else:
        # Incorrect username or password
        return "<p>Incorrect username or password</p>" + redirect(url_for('admin_login'))

@app.route('/flag.html')
def flag():
    return render_template('flag.html')

if __name__ == '__main__':
    app.run(debug=True)
