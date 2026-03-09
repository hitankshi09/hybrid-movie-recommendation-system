import streamlit as st
from hybrid_model import hybrid_recommendation

st.title("Hybrid Movie Recommendation System")

movie_name = st.text_input("Enter Movie Name")

if st.button("Recommend"):

    recs = hybrid_recommendation(movie_name)

    for movie in recs:
        st.write(movie)