# Movie Database CLI

A command-line interface (CLI) application for managing a personal movie database. This tool allows you to add, delete, update, and view movies. It fetches movie data from an external API, stores it in an SQLite database, and can generate a simple static website to display your collection.

## Features

- **List Movies**: View all movies in your database with their ratings and release years.
- **Add Movie**: Add a new movie by title. Data (year, rating, poster) is fetched automatically from an API.
- **Delete Movie**: Remove a movie from your collection.
- **Update Movie**: Change the rating of an existing movie.
- **View Stats**: Get statistics like average/median rating, and see the best/worst movies.
- **Get Random Movie**: Get a random movie suggestion from your database for movie night.
- **Search**: Search for movies in your collection by title.
- **Sort by Rating**: Display movies sorted from highest to lowest rating.
- **Generate Histogram**: Create a PNG image showing the distribution of movie ratings.
- **Generate Website**: Automatically generate a static `index.html` file to visually browse your movie posters.

## Project Structure

```
.
├── .env
├── .env.example
├── .gitignore
├── data/
│   └── movies.db
├── output/
│   ├── index.html
│   └── ratings.png
├── src/
│   ├── api_handler.py
│   ├── main.py
│   ├── movie_display.py
│   ├── storage_manager.py
│   └── website_generator.py
├── template/
│   ├── index_template.html
│   └── style.css
└── requirements.txt
```

## Setup & Installation

Follow these steps to get the project running on your local machine.

**1. Clone the repository:**
```bash
git clone https://github.com/unRekable/Movies-with-DB
cd Movies-with-DB
```

**2. Create a virtual environment:**
```bash
python -m venv venv
```

**3. Activate the virtual environment:**
- On Windows: `.\venv\Scripts\activate`
- On macOS/Linux: `source venv/bin/activate`

**4. Install dependencies:**
```bash
pip install -r requirements.txt
```

**5. Configure environment variables:**
Create a `.env` file in the root directory by copying the `.env.example` file.
```bash
cp .env.example .env
```
Now, open the `.env` file and fill in the required values:
```ini
# .env
API_KEY="your_omdb_api_key"
APP_NAME="My Movie Collection"
```

## Usage

To run the application, execute the `main.py` script from the root directory:

```bash
python src/main.py
```

You will be presented with a menu of options to manage and view your movie database. Generated files like `ratings.png` and `index.html` will be saved in the `output/` directory.