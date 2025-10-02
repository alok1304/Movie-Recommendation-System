import pickle
import streamlit as st
import requests

# Function to fetch movie poster from TMDb API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=3261fcf9376dffbb4e4e28cfaca32f8a&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise error for bad status codes
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie_id {movie_id}: {e}")
        return None


# Recommendation function based on cosine similarity
def recommend(movie, num_recommendations=5):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:1+num_recommendations]:
        recommended_movie_names.append(movies.iloc[i[0]].title)
        movie_id = movies.iloc[i[0]].movie_id
        poster = fetch_poster(movie_id)
        recommended_movie_posters.append(poster)
    return recommended_movie_names, recommended_movie_posters

# --- Streamlit App ---
st.title("🎬 Movie Recommender System")

# Load preprocessed movies and similarity matrix
movies = pickle.load(open('models/movie_list.pkl','rb'))  # Should include 'tags', 'movie_id', 'vote_average'
similarity = pickle.load(open('models/similarity.pkl','rb'))

# --- Sidebar Filters ---
st.sidebar.header("Filter Movies")

# Keyword search
search_keyword = st.sidebar.text_input("Search by keyword in title:")

# Rating filter
if 'vote_average' in movies.columns:
    min_rating = float(movies['vote_average'].min())
    max_rating = float(movies['vote_average'].max())
    selected_rating = st.sidebar.slider("Minimum Rating", min_rating, max_rating, min_rating)
else:
    selected_rating = 0

# Number of recommendations
num_recommendations = st.sidebar.slider("Number of Recommendations", 1, 10, 5)

# --- Filter movies based on sidebar selections ---
filtered_movies = movies.copy()

# Keyword search filter
if search_keyword:
    filtered_movies = filtered_movies[filtered_movies['title'].str.contains(search_keyword, case=False)]

# Rating filter
if 'vote_average' in movies.columns:
    filtered_movies = filtered_movies[filtered_movies['vote_average'] >= selected_rating]

# Dropdown for movie selection
movie_list = filtered_movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown:", movie_list)

# --- Show Recommendations ---
if st.button('Show Recommendations'):
    if selected_movie:
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie, num_recommendations)
        cols = st.columns(num_recommendations)
        placeholder_url = "https://via.placeholder.com/200x300?text=No+Image"
        for i, col in enumerate(cols):
            col.text(recommended_movie_names[i])
            col.image(recommended_movie_posters[i] if recommended_movie_posters[i] else placeholder_url)
    else:
        st.warning("Please select a movie to get recommendations.")
