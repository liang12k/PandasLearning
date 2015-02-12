import pandas as pd

# # avoids ParserWarning; pass in arg 'engine="python"'
pd_read_table = pd.io.parsers.read_table

# # set up users DataFrame; colnames == unames
unames = ["user_id", "gender", "age", "occupation", "zip"]
# users = pd.read_table("users.dat", sep="::", header=None, names=unames)
users = pd_read_table("users.dat", sep="::", header=None, 
                     names=unames, engine="python")

# # set up ratings DataFrame; colnames == rnames
rnames = ["user_id", "movie_id", "rating", "timestamp"]
# ratings = pd.read_table("ratings.dat", sep="::", header=None, names=rnames)
ratings = pd_read_table("ratings.dat", sep="::", header=None, 
                       names=rnames, engine="python")

# # set up movies DataFrame; colnames == mnames
mnames = ["movie_id", "title", "generes"]
# movies = pd.read_table("movies.dat", sep="::", header=None, names=mnames)
movies = pd_read_table("movies.dat", sep="::", header=None, 
                      names=mnames, engine="python")

# print users[:5]
# print ratings[:5]
# print movies[:3]
# print ratings # [1000209 rows x 4 columns]

# # nested merge; ((ratings x users) x movies)
data = pd.merge(pd.merge(ratings, users), movies)
# print data # [1000209 rows x 10 columns]
# print data.ix[0] # print index 0; first row

# # rows, cols are deprecated
# mean_ratings = data.pivot_table("rating", rows="title", cols="gender", 
#                                aggfunc="mean")
# # pivot on "rating" DataFrame; index col = "title", mean on "gender"
mean_ratings = data.pivot_table(
    "rating",
    index="title",
    columns="gender",
    aggfunc="mean",
)
print mean_ratings[:5]
