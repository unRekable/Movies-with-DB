import sys
import textwrap
from colorama import init, Fore, Style
import storage_manager as storage
from movie_display import (
    list_movies,
    stats,
    random_movie,
    search_movie,
    sort_movies,
    create_rating_histogram
)
from website_generator import generate_website

# Initialize colorama for cross-platform terminal color support
init(autoreset=True)


def main():
    """Main program loop to interact with the user and manage the movie database."""

    actions = {
        "0": sys.exit,
        "1": list_movies,
        "2": lambda: storage.add_movie(
            input(f"{Style.BRIGHT}{Fore.YELLOW}Enter the new movie name: ")
        ),
        "3": lambda: storage.delete_movie(
            input(f"{Style.BRIGHT}{Fore.YELLOW}Enter the movie name to delete: ")
        ),
        "4": lambda: storage.update_movie(
            input(f"{Style.BRIGHT}{Fore.YELLOW}Enter movie name: "),
            float(input(f"{Style.BRIGHT}{Fore.YELLOW}Enter new movie rating (0-10): "))
        ),
        "5": stats,
        "6": random_movie,
        "7": search_movie,
        "8": sort_movies,
        "9": lambda: (
            filename := input(f"{Style.BRIGHT}{Fore.YELLOW}Enter filename for histogram (e.g., ratings.png): "),
            create_rating_histogram(filename if filename else "ratings.png")
        ),
        "10": generate_website
    }

    print(f"{Style.BRIGHT}{Fore.MAGENTA}********** My Movies Database **********")

    menu_text = Fore.GREEN + Style.BRIGHT + textwrap.dedent("""
    Menu:
    0. Exit
    1. List movies
    2. Add movie
    3. Delete movie
    4. Update movie
    5. Stats
    6. Random movie
    7. Search movie
    8. Movies sorted by rating
    9. Create Rating Histogram
    10. Generate website
    """)

    while True:
        print(menu_text)
        user_choice = input(f"{Style.BRIGHT}{Fore.YELLOW}Enter choice (0-10): ")
        print()

        action_to_run = actions.get(user_choice)
        if action_to_run:
            try:
                action_to_run()
            except Exception as e:
                print(f"{Fore.RED}An unexpected error occurred: {e}")
            input(f"{Style.BRIGHT}{Fore.BLUE}\nPress enter to continue")
        else:
            print(f"{Fore.RED}Invalid choice. Please select from the menu.")


if __name__ == "__main__":
    main()