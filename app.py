import pickle
import streamlit as st
import requests
import time

st.set_page_config(page_title='Movie Recommender System', page_icon='🎬')
def fetch_poster(movie_id, max_retries=3, retry_delay=1):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for request errors
            
            data = response.json()
            poster_path = data.get('poster_path')
            
            if poster_path:
                full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
                return full_path
            else:
                return None
            
        except requests.RequestException as e:
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
            else:
                return None

    return None


def recommend(movie):
    index = movies[movies['title'] == movie].index
    if not index.empty:
        index = index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[1:6]:
            # fetch the movie poster
            movie_id = movies.iloc[i[0]].get('movie_id')
            if movie_id:
                poster_url = fetch_poster(movie_id)
                if poster_url:
                    recommended_movie_posters.append(poster_url)
                    recommended_movie_names.append(movies.iloc[i[0]].get('title'))
            else:
                st.warning("Movie ID not found for a recommended movie.")
        return recommended_movie_names, recommended_movie_posters
    else:
        st.warning("Movie not found in the dataset.")
        return [], []

st.header('Movie Recommender System Using Machine Learning')

try:
    movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
    similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))
except FileNotFoundError as e:
    st.error(f"Error loading pickle files: {e}")
    st.stop()

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    if recommended_movie_names and recommended_movie_posters:
        col1, col2, col3, col4, col5 = st.columns(5)
        for i in range(min(len(recommended_movie_names), 5)):
            with locals()[f"col{i+1}"]:
                st.text(recommended_movie_names[i])
                st.image(recommended_movie_posters[i])
    else:
        st.warning("No recommendations available for this movie.")
st.markdown(
    """
    <style>
       
        .stApp {
            background-color: #d1ef71 /* Black background for the app */
        }
        .stSelectbox {
          color:white;
        }
        .stText {
            color: white; /* White text */
        }
         .stButton button {
        background-color: white; /* White background */
        color: black; /* Black text */
        padding: 10px 20px; /* Padding for button */
        border: none; /* No border */
        border-radius: 5px; /* Rounded corners */
        cursor: pointer; /* Pointer cursor */
        transition: background-color 0.3s ease, color 0.3s ease; /* Smooth transitions */
    }
    .stButton button:hover {
        background-color: #f0f0f0; /* Light gray background on hover */
    }
    .stButton button:focus {
        outline: none; /* Remove outline on focus */
    }
    .stButton button:active {
        background-color: #d9d9d9; /* Lighter gray background on click */
    }
    .stButton button span {
        color: black; /* Ensure text color remains black */
    }.stButton button {
        background-color: white; /* White background */
        color: black !important; /* Black text */
        padding: 10px 20px; /* Padding for button */
        border: none; /* No border */
        border-radius: 5px; /* Rounded corners */
        cursor: pointer; /* Pointer cursor */
        transition: background-color 0.3s ease, color 0.3s ease; /* Smooth transitions */
    }
    .stButton button:hover {
        background-color: #f0f0f0; /* Light gray background on hover */
    }
    .stButton button:focus {
        outline: none; /* Remove outline on focus */
    }
    .stButton button:active {
        background-color: #d9d9d9; /* Lighter gray background on click */
    }
    .stButton button span {
        color: black !important; /* Ensure text color remains black */
    }
        .stWarning {
            color: #FF1E39; /* Red warning text */
            font-weight: bold; /* Bold text */
        }
      
       .stSelectbox label {
            color: white; /* Netflix red for selectbox label */
        }
       
    </style>
    """,
    unsafe_allow_html=True
)
