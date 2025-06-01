import os, requests, dotenv
from colorama import Fore, Style

dotenv.load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")

def get_movie_by_title(name):
    try:
        if not name:
            print(f"{Style.BRIGHT}{Fore.YELLOW}Please enter a movie title.")
            return

        req = requests.get(API_URL + "?apikey=" + API_KEY + "&t=" + name)
        req.raise_for_status()
        result = req.json()

        if "Error" in result:
            print(f"{Style.BRIGHT}{Fore.RED}{result['Error']}".replace("Movie not found!", f"Movie '{name}' not found, please try again!"))
            return

        return result

    except requests.exceptions.HTTPError as error:
        print(f"{Style.BRIGHT}{Fore.RED}HTTP Error: {error}")
    except requests.exceptions.ReadTimeout as error:
        print(f"{Style.BRIGHT}{Fore.RED}Time out: {error}")
    except requests.exceptions.ConnectionError as error:
        print(f"{Style.BRIGHT}{Fore.RED}Connection error: {error}")
    except requests.exceptions.RequestException as error:
        print(f"{Style.BRIGHT}{Fore.RED}Exception request: {error}")