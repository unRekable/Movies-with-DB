import os, requests, dotenv

dotenv.load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")

def get_movie_by_title(name):
    try:
        print(API_URL + "?apikey=" + API_KEY + "&t=" + name)

        req = requests.get(API_URL + "?apikey=" + API_KEY + "&t=" + name)
        result = req.json()
        print(result)

        if "Error" in result and result["Error"] == "Movie not found!":
            print(f"Movie {name} not found, please try again!")
            return

        return result["Title"], result["Year"], result["imdbRating"]

    except requests.exceptions.HTTPError as error:
        print("HTTP Error: ", error)
    except requests.exceptions.ReadTimeout as error:
        print("Time out: ", error)
    except requests.exceptions.ConnectionError as error:
        print("Connection error: ", error)
    except requests.exceptions.RequestException as error:
        print("Exception request: ", error)

get_movie_by_title("Titanic")