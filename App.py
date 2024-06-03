import streamlit as st
import pickle
import pandas as pd
import requests

def fetch(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=39137600d3a725a4813e9b4d030a033a&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []
    recommended_movie_poster=[]

    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id

        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch(movie_id))

    return recommended_movie,recommended_movie_poster

movies_list=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_list)
similarity=pickle.load(open('similarity.pkl','rb'))


st.header('Movie Recommendation System')

selected = st.selectbox('Enter the movie name',
                      movies['title'].values)

if st.button('Recommend Movie'):
    names,poster=recommend(selected)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])