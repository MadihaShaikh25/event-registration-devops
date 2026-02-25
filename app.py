from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        college = request.form.get("college")
        department = request.form.get("department")
        year = request.form.get("year")
        event = request.form.get("event")

        return f"""
        <html>
        <head>
            <title>Registration Success</title>
        </head>
        <body style="font-family: Arial; background:#f4f6f9; padding:40px;">
            <h2 style="color:#2c3e50;">🎉 Registration Successful!</h2>
            <hr>
            <p><b>Name:</b> {name}</p>
            <p><b>Email:</b> {email}</p>
            <p><b>Phone:</b> {phone}</p>
            <p><b>College:</b> {college}</p>
            <p><b>Department:</b> {department}</p>
            <p><b>Year:</b> {year}</p>
            <p><b>Event:</b> {event}</p>
            <br>
            <a href="/">Register Another Response</a>
        </body>
        </html>
        """

    return render_template("register.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)