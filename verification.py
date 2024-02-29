from flask import Flask, request, render_template
import ssl

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
            with open('flag.html') as f:
                html = f.read()
                return html
        else:
            with open('adminlog1.html') as f:
                html = f.read()
                return html
    else:
        return render_template('adminlog.html')

if __name__ == '__main__':
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain('cert.pem', 'key.pem')
    app.run(debug=True, ssl_context=context)
