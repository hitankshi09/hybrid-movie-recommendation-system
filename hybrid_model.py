from content_model import get_similar_movies

def hybrid_recommendation(movie_title):

    content_recs = get_similar_movies(movie_title)

    return content_recs