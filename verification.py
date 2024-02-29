from flask import Flask, request, render_template

app = Flask(__name__)

def validate_password(username, password):
    """Validates if the given username and password match the expected values."""
    expected_username = "admin"
    expected_password = "zxcvbnm"

    if username == expected_username and password == expected_password:
        return True
    else:
        return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if validate_password(username, password):
            return render_template('flag.html')
        else:
            return render_template('adminlog1.html')
    else:
        return render_template('adminlog.html')

if __name__ == '__main__':
    app.run(debug=True)
