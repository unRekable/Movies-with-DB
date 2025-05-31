import os, json
from dotenv import load_dotenv
from colorama import Fore

load_dotenv()

DB_FILENAME = os.getenv("DB_FILENAME")

def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies_db information in the database.

    The function loads the information from the JSON
    file and returns the db.

    For example, the function may return:
    {
      "Titanic": {
        "rating": 9,
        "year": 1999
      },
      "..." {
        ...
      },
    }

    If the database is empty, it will return an empty dictionary.
    """
    if not os.path.exists(DB_FILENAME):
        print(f"{Fore.YELLOW}Info: '{DB_FILENAME}' not found. Starting with empty database.")
        return {}
    try:
        with open(DB_FILENAME, "r") as json_file:
            data = json.load(json_file)
            if not isinstance(data, dict):
                print(f"{Fore.RED}Error: Invalid db format in '{DB_FILENAME}'. Starting empty.")
                return {}
            return data
    except json.JSONDecodeError:
        print(f"{Fore.RED}Error: Cannot decode JSON from '{DB_FILENAME}'. Starting empty.")
        return {}
    except Exception as e:
        print(f"{Fore.RED}Error loading '{DB_FILENAME}': {e}. Starting empty.")
        return {}


def save_movies(movies_db):
    """
    Saves the movie information in the database.
    :param movies_db:
    :return:
    """
    try:
        with open(DB_FILENAME, "w") as json_file:
            json.dump(movies_db, json_file)
    except FileNotFoundError:
        print(f"{Fore.RED}{DB_FILENAME} not found")




