import app as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distance = similarities[movie_index]
    movies_list = sorted(list(enumerate(distance)),reverse=True, key = lambda x:x[1])[1:6]
    
    recommended_movie = []
    recommended_movie_posters=[]
    
    for i in movies_list:
       id= movies.iloc[i[0]].movie_id
       recommended_movie.append(movies.iloc[i[0]].title)
       recommended_movie_posters.append(fetch_poster(id))
    return recommended_movie,recommended_movie_posters
        
          
    
    

movie_dict = pickle.load(open("movie_dict.pkl","rb"))
movies = pd.DataFrame(movie_dict)

similarities= pickle.load(open("similarities.pkl","rb"))

st.title("Movie Recommentation System")

seleted_movie_name = st.selectbox(
"How would you like to be contacted?",
movies["title"].values
)

if st.button("Recommended"):
    name,posters =recommend(seleted_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col2:
        st.text(name[1])
        st.image(posters[1])

    with col3:
        st.text(name[2])
        st.image(posters[2])
    with col4:
        st.text(name[3])
        st.image(posters[3])
    with col5:
        st.text(name[4])
        st.image(posters[4])


