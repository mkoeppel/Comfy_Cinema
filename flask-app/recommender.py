"""Machine-Learning Code that returns movie recommendations"""
import numpy as np
from sklearn.decomposition import NMF
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import joblib as jb
from config import OMDb_KEY

MOVIES = pd.read_csv("./ml-latest-small/movies.csv")
RATINGS = pd.read_csv("./ml-latest-small/ratings.csv")
LINKS = pd.read_csv("./ml-latest-small/links.csv")
DF = pd.merge(RATINGS, MOVIES, on="movieId")

MIDS = RATINGS["movieId"].unique()
MIDS = pd.DataFrame(MIDS)
MOVIES_DF = pd.merge(MIDS, MOVIES, left_on=0, right_on="movieId")

model_jb = jb.load("./nmf_model2.joblib")
P = model_jb.components_

def calculate_best_movies(movies, ratings):
    """
    uses a predifined NMF model to predict movies most likely to fit with the input movies and ratings

    input:
        the movies and ratings provided on the index- and ratings-html sites
    output:
        3 posters of new movies the user likely to enjoy
    """
    user = {"title" : movies, "rating" : ratings}
    user = pd.DataFrame(user)

    user_ratings = pd.merge(MOVIES_DF, user, on="title", how="left")
    new_user = user_ratings["rating"].fillna(2.5)
    new_u = np.array(new_user).reshape(1, -1)
    profile = model_jb.transform(new_u)
    result = np.dot(profile, P)
    MOVIES_DF["recom"] = result.T

    rec_movies = MOVIES_DF.sort_values("recom", ascending=False)
    rec_movies = rec_movies.merge(user.drop_duplicates(), on=["title"],
                   how='left', indicator=True)
    rec_movies = rec_movies[rec_movies['_merge'] == 'left_only']
    imdb_id = pd.merge(rec_movies, LINKS, on="movieId").head(3)
    nmf_img = []
    for i in imdb_id["imdbId"].apply("{:0>7}".format):
        nmf_img.append("https://img.omdbapi.com/?apikey="+OMDb_KEY+"&i=tt"+i+"&h=200")
    return nmf_img

def similar_users_recommender(movies, ratings):
    """
    uses a cosine-similarity matrix to predict movies most likely to fit with the input movies and ratings

    input:
        the movies and ratings provided on the index- and ratings-html sites
    output:
        3 posters of new movies the user probably likes
    """
    user = {"title" : movies, "rating" : ratings}
    user = pd.DataFrame(user)
    user_ratings = pd.merge(MOVIES_DF, user, left_on="title", right_on="title", how="left")
    query = user_ratings["rating"]
    query = np.array(query)

    m_matrix = DF.pivot_table(values="rating", index="userId", columns="movieId")
    m_matrix.loc["e"] = query
    m_matrix = m_matrix.sub(m_matrix.mean(axis=0), axis=1)
    m_matrix.fillna(0, inplace=True)

    cosim = cosine_similarity(m_matrix)[-1]
    cosim = pd.DataFrame(cosim)
    top10 = cosim.sort_values(by=[0], ascending=[False]).head(11)
    similar_users = list(top10.index)
    similar_users = similar_users[1:]

    users_r = m_matrix.loc[similar_users, :]
    movie_ratings_avg = users_r.mean()
    movie_ratings_avg = pd.DataFrame(movie_ratings_avg)

    rec_movies = movie_ratings_avg.sort_values(by=[0], ascending=[False])
    rec_movies = pd.merge(rec_movies, MOVIES, on="movieId", how="left")
    rec_movies = rec_movies.merge(user.drop_duplicates(), on=["title"],
                   how='left', indicator=True)
    rec_movies = rec_movies[rec_movies['_merge'] == 'left_only']
    imdb_id = pd.merge(rec_movies, LINKS, on="movieId").head(3)
    cos_img = []
    for i in imdb_id["imdbId"].apply("{:0>7}".format):
        cos_img.append("https://img.omdbapi.com/?apikey="+OMDb_KEY+"&i=tt"+i+"&h=200")
    return cos_img

def movieId_to_title(ids):
    """ Given a list of movieIds, returns a corresponding list of movie titles."""
    return MOVIES.set_index("movieId").loc[ids]["title"].tolist()
