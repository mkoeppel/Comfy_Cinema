# Movie Recommender
a python and sklearn based program that recommends movies based on user input

### This movie recommender helps you select the movie, you're really gonna enjoy watching next!
### It works best, if you select 5 or more movies you liked (or hated) and give them some ratings from 0-5.

As output you get two different kinds of suggestions: \
  1: This is based on an unsupervised non-negative matrix factorization approach (NMF). \
  2: The second set of suggestions come from a cosine-similarity a.k.a. collaborative filtering approach.

Both give you 5 different suggestions, as you will find out they only sometimes overlap.
\
This runs on the movielens dataset (as of now on it's small version 'ml-latest-small' with approximatley 100 k ratings). It can be found here:
https://grouplens.org/datasets/movielens/

To make the recommender work git clone the repository to your computer, navigate into the flask-app, enter 'python app.py' in the terminal and copy 'http://127.0.0.1:5000/' into the address-field of your browser. \

It also runs on a heroku-server:

https://movie-couch.herokuapp.com/

### to do:
add user-comments for the suggested movies
scale up database for better recommendations
add impressum
