"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



# Replace this with routes and view functions!
@app.route('/')
def show_homepage():
    return render_template('homepage.html')

@app.route('/movies')
def show_movies():
    """View all movies."""
    movies = crud.get_movies()
    return render_template('all_movies.html', movies=movies)

@app.route('/movie/<int:id>')
def show_movie_details(id):
    """View details for a specific movie."""
    movie = crud.get_movie_by_id(id)
    return render_template('movie_details.html', movie=movie)

@app.route('/users')
def show_users():
    """View all users."""
    users = crud.get_users()
    return render_template('all_users.html', users=users)

@app.route('/users', methods=['POST'])
def register_user():
    """Create new user."""
    email = request.form.get("email")
    password = request.form.get("password")
    if crud.get_user_by_email(email):
        flash("This email already exists. Please try again.")
    else:
        crud.create_user(email, password)
        flash("Account created successfully. Please log in.")
    return redirect("/")

@app.route('/user/<int:id>')
def show_user_profile(id):
    """View details for a specific movie."""
    user = crud.get_user_by_id(id)
    return render_template('userprofile.html', user=user)

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
