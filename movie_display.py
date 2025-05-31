import statistics, random, os
import matplotlib.pyplot as plt
from collections import Counter
from colorama import Fore, Style
from difflib import get_close_matches
from sqlalchemy import create_engine, text
import storage_manager as storage

# Define the database URL
DB_URL = "sqlite:///movies.db"

# Create the engine
engine = create_engine(DB_URL, echo=True)

def list_movies():
     """Display all movies and their ratings from the DB."""
     movies = storage.get_movies()
     print(f"{Style.BRIGHT}{Fore.GREEN}{len(movies)} in total")
     for movie, data in movies.items():
         print(f"{Style.BRIGHT}{Fore.WHITE}{movie} ({data['year']}): {data['rating']}")

def stats():
    """Display average, median, best and worst movie ratings. If multiple movies_db share the highest or lowest rating, all are displayed."""
    movies = storage.get_movies()

    if not movies:
        print(f"{Fore.RED}No movies in the database to calculate stats.")
        return

    ratings = []

    for movie in movies:
        ratings.append(movies[movie]['rating'])

    avg_rating = sum(ratings) / len(ratings)
    median_rating = statistics.median(ratings)
    print(f"{Style.BRIGHT}{Fore.CYAN}Average rating: {Style.BRIGHT}{Fore.WHITE}{avg_rating:.2f}")
    print(f"{Style.BRIGHT}{Fore.CYAN}Median rating: {Style.BRIGHT}{Fore.WHITE}{median_rating:.2f}")

    max_rating = max(ratings)
    min_rating = min(ratings)

    best_movies = [title for title, title_info in movies.items() if title_info['rating'] == max_rating]
    worst_movies = [title for title, title_info in movies.items() if title_info['rating'] == min_rating]

    best_movies_str = ", ".join(best_movies)
    best_label = "Best movie" if len(best_movies) == 1 else "Best movies_db"
    print(f"{Style.BRIGHT}{Fore.GREEN}{best_label}: {Style.BRIGHT}{Fore.WHITE}{best_movies_str} ({max_rating})")

    worst_movies_str = ", ".join(worst_movies)
    worst_label = "Worst movie" if len(worst_movies) == 1 else "Worst movies_db"
    print(f"{Style.BRIGHT}{Fore.RED}{worst_label}: {Style.BRIGHT}{Fore.WHITE}{worst_movies_str} ({min_rating})")


def random_movie(movies_db):
    """Select and display a random movie from the database."""
    if not movies_db:
        print(f"{Fore.RED}No movies_db in the database to display a random movie.")
        return

    title, title_info = random.choice(list(movies_db.items()))
    print(
        f"{Style.BRIGHT}{Fore.MAGENTA}Your movie for tonight: {title}, it's rated {title_info['rating']} and from {title_info['year']}.")


def search_movie(movies_db):
    """Search for movies_db by title using substring and fuzzy matching."""
    if not movies_db:
        print(f"{Fore.RED}No movies_db in the database to search.")
        return

    user_search = input(f"{Style.BRIGHT}{Fore.YELLOW}Enter part of the movie name: ")
    found = False
    for title in movies_db.keys():
        if user_search.lower() in title.lower():
            print(
                f"{Style.BRIGHT}{Fore.WHITE}{title} ({movies_db[title]['year']}): {movies_db[title]['rating']}")
            found = True

    if not found:
        titles = list(movies_db.keys())
        suggestions = get_close_matches(user_search, titles, n=5, cutoff=0.3)
        if suggestions:
            print(f'{Fore.RED}\nThe movie "{user_search}" does not exist. Did you mean:')
            for suggestion in suggestions:
                print(
                    f"{Style.BRIGHT}{Fore.CYAN}{suggestion}, Year: {movies_db[suggestion]['year']}, Rating: {movies_db[suggestion]['rating']}")
        else:
            print(f'{Fore.RED}\nNo movie found for "{user_search}".')


def sort_movies(movies_db):
    """Sort and display movies_db by rating in descending order."""
    if not movies_db:
        print(f"{Fore.RED}No movies_db in the database to sort.")
        return

    movies_sorted_keys = sorted(
        movies_db.keys(),
        key=lambda movie_key: movies_db[movie_key]['rating'],
        reverse=True
    )

    print(f"{Style.BRIGHT}{Fore.CYAN}Movies sorted by rating:")
    for movie_key in movies_sorted_keys:
        rating = movies_db[movie_key].get('rating', 'N/A')
        year = movies_db[movie_key].get('year', 'N/A')
        print(f"{Style.BRIGHT}{Fore.WHITE}{movie_key} ({year}): {rating}")


def create_rating_histogram(movies_db, filename):
    """Create and save a histogram of movie ratings to a file."""
    if not movies_db:
        print(f"{Fore.RED}No movies_db in the database to create a histogram.")
        return

    ratings = []

    for movie in movies_db:
        ratings.append(movies_db[movie]['rating'])

    counts = Counter(ratings)
    sorted_items = sorted(counts.items())
    labels = [str(rating) for rating, _ in sorted_items]
    heights = [count for _, count in sorted_items]

    plt.bar(labels, heights, edgecolor='black')
    plt.xlabel("Rating")
    plt.ylabel("Number of Movies")
    plt.title("Movie Rating Distribution")
    plt.yticks(range(0, max(heights) + 1))
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"{Style.BRIGHT}{Fore.GREEN}Histogram saved in {os.getcwd()} as '{filename}'")