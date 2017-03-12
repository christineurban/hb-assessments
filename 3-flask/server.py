from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

JOBS = ["software engineer", "QA engineer", "product manager"]


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def index():
    """Return homepage."""

    return render_template("index.html")


@app.route("/application-form")
def app_form():
    """Return application page."""

    return render_template("application-form.html",
                           jobs=JOBS)


@app.route("/application-success")
def app_success():
    """Return confirmation page."""

    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    salary = request.args.get("salary")
    jobtype = request.args.get("jobtype")

    return render_template("application-response.html",
                           firstname=firstname,
                           lastname=lastname,
                           salary=salary,
                           jobtype=jobtype)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
