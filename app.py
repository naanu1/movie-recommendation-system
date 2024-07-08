import pickle
import streamlit as st
import requests

st.set_page_config(page_title='Movie Recommender System', page_icon='🎬')
def fetch_poster(movie_id):
    api_key = "f10aeb4e2a51eed6ea14951bf5ee13ec"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404)
        data = response.json()
        poster_path = data.get('poster_path')  # Use .get() to safely access poster_path
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500" + poster_path
            return full_path
        else:
            # Return a placeholder image URL if poster is not available
            return "https://via.placeholder.com/500x750.png?text=Poster+Not+Available"
    except requests.RequestException as e:
        # Handle connection errors or invalid URLs gracefully
        print("Error fetching movie poster:", e)
        return "https://via.placeholder.com/500x750.png?text=Poster+Not+Available"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        poster = fetch_poster(movie_id)
        recommended_movie_posters.append(poster)
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

st.header('Movie Recommender System')
movies = pickle.load(open('movie_list_compressed.pkl.xz', 'rb'))
similarity = pickle.load(open('similarity_compressed.pkl.xz', 'rb'))


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)
    for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
        with col:
            st.text(name)
            st.image(poster)
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
