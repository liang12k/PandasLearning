import pandas as pd

unames = ["user_id", "gender", "age", "occupation", "zip"]
users = pd.read_table("users.dat", sep="::", header=None, names=unames)

rnames = ["user_id", "movie_id", "rating", "timestamp"]
ratings = pd.read_table("ratings.dat", sep="::", header=None, names=rnames)

mnames = ["movie_id", "title", "generes"]
movies = pd.read_table("movies.dat", sep="::", header=None, names=mnames)

# print users[:5]
# print ratings[:5]
# print movies[:3]
# print ratings # [1000209 rows x 4 columns]

data = pd.merge(pd.merge(ratings, users), movies)
# print data # [1000209 rows x 10 columns]
print data.ix[0]
