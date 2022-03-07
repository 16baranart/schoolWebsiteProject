import backEnd as BE
import flask
import os

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)


# HOME PAGE ------------------------------------------------------------------------------------------- #
@app.route("/") # If you type in website.com/, it redirects you to website.com/home
@app.route("/home") # The following function is what happens when you go to website.com/home
def home():
    flask.flash("hi")
    return flask.render_template("home.html") # Passes the "posts" variable to the homepage, so they can be installed


@app.route("/posts")
def posts():
    dicList = BE.sortCollection(BE.makeDB(), "date+time", False)
    return flask.render_template("posts.html", dictionaries = dicList)

# RUN ------------------------------------------------------------------------------------------------- #
if __name__ == "__main__": # Will only run if the program has
    #BE.displayInCollection()
    app.run(debug=True) # Debug=True allows the program's changes to take effect during runtime
