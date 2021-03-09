# Movie Recommender

### This movie recommender helps you select the movie, you're really gonna enjoy watching next!
### It works best, if you select 5 or more movies you liked (or hated) and give them some ratings from 0-5.

As output you get two different kinds of suggestions: \
  1: This is based on an unsupervised non-negative matrix factorization approach (NMF). \
  2: The second set of suggestions come from a cosine-similarity a.k.a. collaborative filtering approach.

Both give you 3 different suggestions, as you will find out they only sometimes overlap (this started as a SPICED bootcamp project and was improved afterwards). \
Movie suggestions are now displayed as posters taken from the omdb-API:
![alt text](https://github.com/mkoeppel/Comfy_Cinema/blob/master/matrix.omdbapi.jpg)
The required API-Key was obtained from https://www.omdbapi.com/ and stored in a config-file, from where it is imported by the recommender script.

### used tech:
![alt text](https://github.com/mkoeppel/Comfy_Cinema/blob/master/Tech_stack_comfy_cinema.png)


This runs on the movielens dataset (as of now on it's small version 'ml-latest-small' with approximatley 100 k ratings). It can be found here:
https://grouplens.org/datasets/movielens/


It now runs on a heroku-server:

https://movie-couch.herokuapp.com/



### to do:
~~add omdb-API to get recommendations as posters~~ \
add user-comments for the suggested movies \
scale up database for better recommendations
