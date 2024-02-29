from flask import Flask, render_template, request

app = Flask(__name__)

# define the login endpoint
@app.route('/login', methods=['POST'])
def login():
    # get form data
    username = request.form['username']
    password = request.form['password']

    # validate form data
    if username == 'admin' and password == '5201314':
        # authentication succeeded
        return 'Authentication succeeded'
    else:
        # authentication failed
        return 'Authentication failed'

# define the admin login page
@app.route('/adminlog')
def admin_login():
    # render the admin login page
    return render_template('adminlog.html', app=app)

if __name__ == '__main__':
    # run the app
    app.run()
