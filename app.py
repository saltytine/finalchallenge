from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Set the configuration variables
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "5201314"

# Define the login view function
@app.route('/login', methods=['GET', 'POST'])
def login():
    # If the form has been submitted
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password match
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            # Password is correct, redirect to flag.html
            return redirect(url_for('flag'))
        else:
            # Incorrect username or password
            return "<p>Incorrect username or password</p>"
    else:
        # If the form has not been submitted, render the login page
        return render_template('adminlog.html')

# Define the flag view function
@app.route('/flag')
def flag():
    # Render the flag page
    return render_template('flag.html')

# Define the macros view function
@app.route('/macros')
def macros():
    # Render the macros.html template
    return render_template('macros.html')

# Define the adminlog.html template
adminlog_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Login</title>
</head>
<body>
    <h1>Admin Login</h1>
    <form method="post" action="{{ url_for('login') }}">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
"""

# Define the flag.html template
flag_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flag</title>
</head>
<body>
    <h1>Flag</h1>
    <!-- Insert flag here -->
</body>
</html>
"""

# Define the macros.html template
macros_html = """
{% macro url_for(endpoint) %}
    {{ url_for(endpoint) }}
{% endmacro %}
"""

if __name__ == '__main__':
    app.run(debug=True)
