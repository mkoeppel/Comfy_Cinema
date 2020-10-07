from flask import Flask, render_template, request
from recommender import calculate_best_movies
from recommender import similar_users_recommender
from recommender import movieId_to_title
import pickle5 as pickle
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)
# make this file the center of the app
# We launch this file from the terminal to start the app

@app.route('/')
@app.route('/index', methods=['POST', 'GET'])  # whatever the function below this, route it to the path
def index():
    movies=[]
    return render_template('index.html')


@app.route('/ratings', methods=['POST', 'GET'])
def ratings():
    user_input = dict(request.form)              # copied from github to make it worl
    print(user_input)
    if 'movielist' in user_input.keys():
        movielist = user_input['movielist']
        ids = list(map(int, movielist.split(',')))
        titles = movieId_to_title(ids)
        movies = dict(zip(titles,ids))
    else:
        movies = dict()
    pkl_filename = "tmp.pkl"
    with open(pkl_filename, 'wb') as file:
        pickle.dump(movies, file)
    print(movies)
    return render_template('ratings.html', movie_list=movies.items())


@app.route('/recommendations', methods=['GET', 'POST'])
def recommender():
    with open("tmp.pkl", 'rb') as file:
        user_input_movies = pickle.load(file)
    user_input_movies = list(user_input_movies)
    user_input_ratings = request.args.getlist('rating_values')
    user_input_ratings = [int(x) for x in user_input_ratings]
    #result = calculate_best_movies(user_input)
    result2 = similar_users_recommender(user_input_movies, user_input_ratings)
    return render_template('recommendations.html', nmf=user_input_movies, cosim=result2)

if __name__ == '__main__':
    # whatever occurs AFTER this line is executed when we run 'python application.py'
    # however, whatever comes AFTER  this line is NOT executed when we IMPORT application.py

    app.run(debug = True)   # this will start an infinite process, i.e. serving our web page.
    #                        # 'debug = True' displays Back-End errors to the browser, which is useful for local development, NOT for production
                            # Also automatically restarts server upon changes to code.
