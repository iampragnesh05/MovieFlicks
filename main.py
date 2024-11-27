from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, TextAreaField
from wtforms.validators import DataRequired, NumberRange
import requests
import os
from dotenv import load_dotenv

load_dotenv('cred.env')

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'  # Database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking for performance
db = SQLAlchemy(app)  # Initialize SQLAlchemy

# CREATE TABLE
class Movie(db.Model):
    __tablename__ = "movies"  # Name of the table
    id = db.Column(Integer, primary_key=True, autoincrement=True)  # Unique ID for each movie
    title = db.Column(String, unique=True, nullable=False)  # Movie title, unique
    year = db.Column(Integer, nullable=False)  # Release year
    description = db.Column(String, nullable=True)  # Movie description
    rating = db.Column(Float, nullable=True)  # Rating of the movie
    ranking = db.Column(Integer, nullable=True)  # Movie ranking
    review = db.Column(String, nullable=True)  # Movie review
    img_url = db.Column(String, nullable=True)  # URL of the movie poster


# with app.app_context():
#     db.create_all()
#     existing_movie  = db.session.query(Movie).filter_by(title="Phone Booth").first()
#     if not existing_movie:
#         new_movie = Movie(
#             title="Phone Booth",
#             year=2002,
#             description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. "
#                         "Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#             rating=7.3,
#             ranking=10,
#             review="My favourite character was the caller.",
#             img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#         )
#
#         # Add the movie to the database
#         db.session.add(new_movie)
#         db.session.commit()
#         print("Movie added successfully!")
#     else:
#         print("Movie already exists in the database.")
#
#         # Add the second movie if not already present
#         second_movie = db.session.query(Movie).filter_by(title="Avatar The Way of Water").first()
#         if not second_movie:
#             second_movie = Movie(
#                 title="Avatar The Way of Water",
#                 year=2022,
#                 description="Set more than a decade after the events of the first film, learn the story of the Sully family "
#                             "(Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, "
#                             "the battles they fight to stay alive, and the tragedies they endure.",
#                 rating=7.3,
#                 ranking=9,
#                 review="I liked the water.",
#                 img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#             )
#             db.session.add(second_movie)
#             db.session.commit()
#             print("Second movie added successfully!")
#         else:
#             print("Second movie already exists in the database.")

# Form to handle movie rating and review
class RateMovieForm(FlaskForm):
    rating = FloatField('Rating', validators=[DataRequired(), NumberRange(min=0, max=10)], render_kw={"step": "0.1", "min": 0, "max": 10})
    review = TextAreaField('Review', validators=[DataRequired()], render_kw={"rows": 4, "cols": 50})
    submit = SubmitField('Submit')

def update_rankings():
    # Fetch all movies sorted by rating in descending order
    movies = Movie.query.order_by(Movie.rating.desc()).all()
    for index, movie in enumerate(movies, start=1):
        movie.ranking = index  # Assign rank based on sorted position
    db.session.commit()  # Commit changes to the database


@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.ranking).all()
    return render_template("index.html", movies=movies)


# Edit Movie Route
@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    form = RateMovieForm(obj=movie)
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()  # Commit changes to the database

        update_rankings()
        return redirect(url_for('home'))

    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete/<int:movie_id>", methods=["POST"])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)  # Fetch the movie by its ID, or return 404 if not found
    db.session.delete(movie)  # Delete the movie
    db.session.commit()  # Commit the change to the database
    return redirect(url_for('home'))  # Redirect back to the home page

# Form for adding a new movie
class AddMovieForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')



# API Request to get movie data
def get_movie_data(title):
    api_key = os.getenv("api_key")  # Replace with your own TMDb API key
    url = f"https://api.themoviedb.org/3/search/movie?query={title}&include_adult=false&language=en-US&page=1&api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            # Extract relevant data for all results
            movies = [
                {
                    'id': movie['id'],  # TMDb movie ID for unique identification
                    'title': movie['title'],
                    'year': movie['release_date'][:4] if 'release_date' in movie else 'Unknown',
                    'description': movie.get('overview', 'No description available'),
                    'rating': movie.get('vote_average', None),
                    'img_url': f"https://image.tmdb.org/t/p/w500{movie.get('poster_path', '')}"
                }
                for movie in data['results']
            ]
            # Return the movie data
            return movies
        else:
            print("No movies found.")
            return []
    else:
        print(f"Error: {response.status_code}")
        return []



@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.movie_title.data
        movie_data = get_movie_data(movie_title)  # Get movie data from the API

        if movie_data:
            return render_template("select.html", movies=movie_data)
        else:
            print("No movie data to add.")


        return redirect(url_for('home'))  # Redirect back to the homepage

    return render_template("add.html", form=form)

@app.route("/select", methods=["POST"])
def select_movie():
    # Get the selected movie data from the form
    title = request.form.get('title')
    year = request.form.get('year')
    description = request.form.get('description')
    rating = request.form.get('rating')
    img_url = request.form.get('img_url')

    # Add the selected movie to the database
    new_movie = Movie(
        title=title,
        year=year,
        description=description,
        rating=rating,
        img_url=img_url
    )
    db.session.add(new_movie)
    db.session.commit()
    update_rankings()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
