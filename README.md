# Movie Recommender

## This movie recommender helps you select the movie, you're really gonna enjoy watching next!
### It works best, if you select 5 or more movies you liked (or hated) and give them some ratings from 0-5.

As output you get two different kinds of suggestions: \
  1: This is based on an unsupervised non-negative matrix factorization approach (NMF). \
  2: The second set of suggestions come from a cosime-similarity a.k.a. collaborative filtering approach.

Both give you 5 different suggestions, as you will find out the only sometimes overlap.
\
This runs on the movielens dataset (as of now on it's small version 'ml-latest-small' with approximatley 100 k ratings). It can be found here:
https://grouplens.org/datasets/movielens/

To make the recommender work git clone the repository to your computer, navigate into the flask-app, enter 'python application.py' in the terminal and copy 'http://127.0.0.1:5000/' into the address-field of your browser
We are planning to put this onto a running server in the near future and will provide the url here as well
