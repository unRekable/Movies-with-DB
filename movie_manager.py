from colorama import Fore, Style
from storage_manager import save_movies, get_movies

def add_movie(title, year, rating, movies_db):
    """
    Adds a movie to the movies_db database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    #movies_db = get_movies()

    if title in movies_db:
        print(f"{Fore.RED}Movie {title} already exists!")
        return

    movies_db.update({title: {"rating": rating, "year": year}})
    save_movies(movies_db)
    print(f"{Style.BRIGHT}{Fore.GREEN}Movie '{title}' ({year}) added with rating {rating}")


def delete_movie(title, movies_db):
    """
    Deletes a movie from the movies_db database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    #movies_db = get_movies()

    if title in movies_db:
        movies_db.pop(title)
        print(f"{Style.BRIGHT}{Fore.GREEN}Movie '{title}' successfully removed from database!")
        save_movies(movies_db)
    else:
        print(f"{Fore.RED}Movie {title} not in database!")

def update_movie(title, rating, movies_db):
    """
    Updates a movie from the movies_db database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    #movies_db = get_movies()

    if title not in movies_db:
        print(f"{Fore.RED}Movie '{title}' doesn't exist!")
        return

    movies_db[title].update({"rating": rating})
    print(f"{Style.BRIGHT}{Fore.GREEN}Movie '{title}' successfully updated to rating {rating}")

    save_movies(movies_db)