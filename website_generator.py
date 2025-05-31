import os
import dotenv

import storage_manager as storage

dotenv.load_dotenv()

APP_NAME = os.getenv("APP_NAME")


def get_template():
    """Reads the HTML template file from the 'template' directory."""
    with open("template/index_template.html", "r") as fileobj:
        return fileobj.read()


def save_html(html):
    """Saves the provided HTML content to 'index.html'."""
    with open("index.html", "w") as fileobj:
        fileobj.write(html)


def generate_html():
    """Generates HTML list items for each movie in the storage."""
    movies = storage.get_movies()
    html_parts = []

    for movie, details in movies.items():
        html_parts.append(f"""
            <li>
                <div class="movie">
                    <img class="movie-poster"
                         src="{details['image_url']}"
                         title=""/>
                    <div class="movie-title">{movie}</div>
                    <div class="movie-year">{details['year']}</div>
                </div>
            </li>
       """)
    return "\n".join(html_parts)


def generate_website():
    """Generates and saves the complete website HTML file."""
    try:
        template = get_template()
        generated_html = generate_html()

        website = template.replace("__TEMPLATE_TITLE__", APP_NAME).replace(
            "__TEMPLATE_MOVIE_GRID__", generated_html
        )

        save_html(website)
        print("The website has been successfully generated!")

    except FileNotFoundError:
        print("Error: The template file 'template/index_template.html' was not found.")
    except IOError as e:
        print(f"An error occurred during a file operation: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")