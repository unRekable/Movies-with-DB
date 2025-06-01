import os
import dotenv
import storage_manager as storage
from colorama import Fore, Style

dotenv.load_dotenv()

APP_NAME = os.getenv("APP_NAME")


def get_template():
    """Reads the HTML template file from the 'template' directory."""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(project_root, 'template', 'index_template.html')
    with open(template_path, "r") as fileobj:
        return fileobj.read()


def save_html(html):
    """Saves the provided HTML content to 'index.html' in the output folder."""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(project_root, 'output', 'index.html')
    with open(output_path, "w") as fileobj:
        fileobj.write(html)
    return output_path


def generate_html_grid():
    """Generates HTML list items for each movie in the storage."""
    movies = storage.get_movies()
    if not movies:
        return "<p>No movies in the database yet. Add some to see them here!</p>"

    html_parts = []
    for movie, details in movies.items():
        html_parts.append(f"""
            <li>
                <div class="movie">
                    <img class="movie-poster" src="{details['image_url']}" title="{movie} - Rating: {details['rating']}">
                    <div class="movie-title">{movie}</div>
                    <div class="movie-year">{details['year']}</div>
                    <div class="movie-rating">{details['rating']}</div>
                </div>
            </li>
       """)
    return "\n".join(html_parts)


def generate_website():
    """Generates and saves the complete website HTML file."""
    try:
        template = get_template()
        movie_grid_html = generate_html_grid()

        website = template.replace("__TEMPLATE_TITLE__", APP_NAME).replace(
            "__TEMPLATE_MOVIE_GRID__", movie_grid_html
        )

        saved_path = save_html(website)
        print(f"{Style.BRIGHT}{Fore.GREEN}Website has been successfully generated at: {saved_path}")

    except FileNotFoundError:
        print(f"{Style.BRIGHT}{Fore.RED}Error: The template file was not found.")
    except IOError as e:
        print(f"{Style.BRIGHT}{Fore.RED}An error occurred during a file operation: {e}")
    except Exception as e:
        print(f"{Style.BRIGHT}{Fore.RED}An unexpected error occurred: {e}")