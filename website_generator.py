import storage_manager as storage

def get_template():
    #movies = storage.get_movies()
    try:
        with open("template/index_template.html", "r") as fileobj:
            template = fileobj.read()
            return template
    except FileNotFoundError:
        print("The template file was not found.")
    except IOError:
        print("An error occurred while reading the template file.")

def generate_html():
   movies = storage.get_movies()
   print(movies)

   for movie in movies:
       print(movie)

def save_html(html):
    try:
        with open("index.html", "w") as fileobj:
            fileobj.write(html)
    except IOError:
        print("An error occurred while writing the html file.")

def generate_website():
    template = get_template()

generate_html()