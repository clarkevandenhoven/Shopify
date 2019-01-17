from flask import render_template
import connexion

# Create the app instance

app = connexion.App(__name__, specification_dir = "./")

# Read the Swagger File to configure the endpoints
app.add_api("swagger.yml")

# Create a URL route for the app in "/"

@app.route("/")
def home():
    """ Responds to browser URL localhost:5000
    :returns the template home.html"""

    return render_template("home.html")

# If in stand alone mode, run the application

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)
