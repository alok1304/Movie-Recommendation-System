# Movie Recommender System

A web-based movie recommendation system built using **Python**, **Streamlit**, and **Machine Learning** techniques. The app suggests movies similar to a selected movie, along with their posters fetched from **The Movie Database (TMDb) API**.

---

## Features

- **Movie Recommendations:** Suggests 5 movies similar to the selected movie.  
- **Movie Posters:** Fetches and displays movie posters using TMDb API.  
- **Interactive UI:** Built with **Streamlit**, allowing easy selection of movies from a dropdown.  

---

## Demo

1. Select a movie from the dropdown menu.  
2. Click **Show Recommendation**.  
3. View recommended movie titles and their posters in a 5-column layout.  

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <repo-folder>
```

2. Create and activate a virtual environment (optional):

```
python -m venv venv
source venv/bin/activate    # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:
```
pip install -r requirements.txt
```

## Ensure the following files exist in the models folder:

movie_list.pkl — list of movies

similarity.pkl — similarity matrix

## Usage

Run the Streamlit app:
```
streamlit run app.py
```

### Select a movie from the dropdown.

#### Click Show Recommendation to see suggested movies with posters.

## How It Works

1. Data Preparation:

- Loaded datasets from TMDb (movies and credits).

- Merged datasets and selected relevant columns: movie_id, title, overview, genres, keywords, cast, crew.

- Cleaned and preprocessed text-based columns for similarity calculations.

2. Similarity Calculation:

- Precomputed a similarity matrix based on movie features.

- Saved processed movie list and similarity matrix as .pkl files.

3. Movie Recommendation:

- Finds movies similar to the selected one using the similarity matrix.

- Fetches movie posters from TMDb API and displays them.


Folder Structure
```
Movie-Recommender/
│
├── models/
│   ├── movie_list.pkl
│   └── similarity.pkl
│
├── app.py
├── requirements.txt
└── README.md
```
