import textwrap
from colorama import init, Fore, Style
#from storage_manager import get_movies
#from movie_manager import add_movie, delete_movie, update_movie
from movie_display import (list_movies, stats, random_movie,
                           search_movie, sort_movies, create_rating_histogram)

#from storage_manager import add_movie, delete_movie, update_movie
import storage_manager as storage

# Initialize colorama for cross-platform terminal color support
init(autoreset=True)

def main():
    """Main program loop to interact with the user and manage movies_db."""
    #movies_db = get_movies()

    actions = {
        "1": lambda: list_movies(),
        "2": lambda: storage.add_movie(
            input(f"{Style.BRIGHT}{Fore.YELLOW}Enter the new movie name: "),
            int(input(f"{Style.BRIGHT}{Fore.YELLOW}Enter new movie year: ")),
            float(input(f"{Style.BRIGHT}{Fore.YELLOW}Enter new movie rating (0-10): "))
        ),
        "3": lambda: storage.delete_movie(
            input(f"{Style.BRIGHT}{Fore.YELLOW}Enter the movie name to delete: ")
        ),
        "4": lambda: update_movie(
            input(f"{Style.BRIGHT}{Fore.YELLOW}Enter movie name: "),
            float(input(f"{Style.BRIGHT}{Fore.YELLOW}Enter new movie rating (0-10): "))
        ),
        "5": lambda: command_stats(),
        "6": lambda: random_movie(),
        "7": lambda: search_movie(),
        "8": lambda: sort_movies(),
        "9": lambda: (
            filename := input(f"{Style.BRIGHT}{Fore.YELLOW}Enter filename to save the histogram (e.g. ratings.png): "),
            create_rating_histogram(movies_db, filename if filename else "ratings.png")
        )
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
    """)

    while True:
        print(menu_text)
        user_choice = input(f"{Style.BRIGHT}{Fore.YELLOW}Enter choice (1-9): ")
        print()

        if user_choice == "0":
            break
        elif user_choice in actions:
            try:
                action_to_run = actions[user_choice]
                action_to_run()
            except Exception as e:
                print(f"{Fore.RED}An unexpected error occurred: {e}")
            input(f"{Style.BRIGHT}{Fore.BLUE}\nPress enter to continue")
        else:
            print(f"{Fore.RED}Invalid choice. Please select from the menu.")

if __name__ == "__main__":
    main()
