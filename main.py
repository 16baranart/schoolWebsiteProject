import backEnd as BE
import flask

app = flask.Flask(__name__)
titles = []
texts = []





# HOME PAGE ------------------------------------------------------------------------------------------- #
@app.route("/") # If you type in website.com/, it redirects you to website.com/home
@app.route("/home") # The following function is what happens when you go to website.com/home
def home():
    dicList = BE.sortCollection(BE.makeDB(), "date+time", False)

    return flask.render_template("home.html", dictionaries = dicList) # Passes the "posts" variable to the homepage, so they can be installed


# RUN ------------------------------------------------------------------------------------------------- #
if __name__ == "__main__": # Will only run if the program has
    #BE.displayInCollection()
    app.run(debug=True) # Debug=True allows the program's changes to take effect during runtime
