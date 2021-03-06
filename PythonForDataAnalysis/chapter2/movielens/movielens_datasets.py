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
# # pivot on "rating" DataFrame; index col = "title",
# # mean on "gender" ratings
mean_ratings = data.pivot_table(
    "rating",
    index="title",
    columns="gender",
    aggfunc="mean",
)
# print mean_ratings[:5]

# # group by "title", get size of Series based on grouped by "title"
# # Reminder: data is merged of 3 DataFrames
ratings_by_title = data.groupby("title").size()
# print ratings_by_title[:10]

# # get titles with min minSize ratings
minSize = 250
active_titles = ratings_by_title.index[ratings_by_title >= minSize]
# print active_titles

# # using active_titles w ratings >= minSize; 
# # index is the titles; "filtering"
mean_ratings = mean_ratings.ix[active_titles]
# print mean_ratings

# # filter films based on females; sort by F col
top_female_ratings = mean_ratings.sort_index(by="F", ascending=False)
# print top_female_ratings[:10]

# # measuring rating disagreement
# # appending "diff" col; sort by "diff" col
mean_ratings["diff"] = mean_ratings["M"] - mean_ratings["F"]
sorted_by_diff = mean_ratings.sort_index(by="diff")
# print sorted_by_diff[:15]
# # reversing row order using list comprehension [::-1]
# print sorted_by_diff[::-1][:15]

# # getting largest disagreement by variance
# # std deviation of rating grouped by title
# # Reminder: data is merging of 3 DataFrames
rating_std_by_title = data.groupby("title")["rating"].std()
# # filter down to active_titles
rating_std_by_title = rating_std_by_title.ix[active_titles]
# print rating_std_by_title.order(ascending=False)[:10]

### # variance: 
### # ---------
### # http://stattrek.com/statistics/dictionary.aspx?definition=variance
### # -numerical value indicate wide difference by group
### # -distinguish between variance of population & variance of sample
### # 
### # http://simple.wikipedia.org/wiki/Variance
### # -in probability theory, statistics measure how far set of numbers is spread out
### # -measure how much something changes

### # TODO: will work on dataset to analyze by genre
