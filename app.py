from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Define the username and password
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "5201314"

@app.route("/adminlog", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        # Get the username and password from the form
        username = request.form["username"]
        password = request.form["password"]

        # Check if the username and password match
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            # Password is correct, redirect to flag.html
            return redirect(url_for("flag"))
        else:
            # Incorrect username or password
            return "<p>Incorrect username or password</p>"

    # Redirect to the login page
    return render_template("adminlog.html")

@app.route("/flag")
def flag():
    # Redirect to the flag page
    return render_template("flag.html")

if __name__ == "__main__":
    app.run(debug=True)
