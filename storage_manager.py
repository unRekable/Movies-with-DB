from sqlalchemy import create_engine, text
from api_handler import get_movie_by_title
import os, dotenv

dotenv.load_dotenv()

DB_URL = os.getenv("DB_URL")

# Create the engine
engine = create_engine(DB_URL, echo=True)

# Create the movies table if it does not exist
with engine.connect() as connection:
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE NOT NULL,
            year INTEGER NOT NULL,
            rating REAL NOT NULL,
            image_url VARCHAR NOT NULL
        )
    """))
    connection.commit()

def get_movies():
    """Retrieve all movies from the database."""
    with engine.connect() as connection:
        result = connection.execute(text("SELECT title, year, rating, image_url FROM movies"))
        movies = result.fetchall()

    return {row[0]: {"year": row[1], "rating": row[2], "image_url": row[3]} for row in movies}

def add_movie(title):
    """Add a new movie to the database."""

    movie = get_movie_by_title(title)

    if movie:
        title = movie["Title"]
        year = movie["Year"]
        rating = movie["imdbRating"]
        image_url = movie["Poster"]
    else:
        return

    with engine.connect() as connection:
        try:
            connection.execute(text("INSERT INTO movies (title, year, rating, image_url) VALUES (:title, :year, :rating, :image_url)"),
                               {"title": title, "year": year, "rating": rating, "image_url": image_url})
            connection.commit()
            print(f"Movie '{title}' added successfully.")
        except Exception as e:
            print(f"Error: {e}")

def delete_movie(title):
    """Delete a movie from the database."""
    with engine.connect() as connection:
        try:
            connection.execute(text("DELETE FROM movies WHERE title = :title"),
                               {"title": title})
            connection.commit()
            print(f"Movie '{title}' deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")

def update_movie(title, rating):
    """Update a movie's rating in the database."""
    with engine.connect() as connection:
        try:
            connection.execute(text("UPDATE movies SET rating = :rating WHERE title = :title"),
                               {"title": title, "rating": rating})
            connection.commit()
            print(f"Movie '{title}' updated successfully.")
        except Exception as e:
            print(f"Error: {e}")