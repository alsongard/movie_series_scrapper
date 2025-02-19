import pandas as pd


data_df = pd.read_csv("../moviescrapper/data/new_movies_data.csv")
print(data_df)
print(data_df.columns)

"""
Index(['movie_category', 'movie_name', 'movie_rating', 'movie_release_year',
       'movie_url'],
      dtype='object')
"""

# dtype is used to check the datatype of a column
data_types = data_df.dtypes
print(data_types)

#  clean data
clean_data_df = data_df.dropna(axis=0)
print(clean_data_df)
print(clean_data_df.dtypes)

# convert column datatype using astype()
# clean_data_df["movie_rating"] = clean_data_df["movie_rating"].astype('float')
# print(clean_data_df.dtypes)

# high_movie_rating_df = clean_data_df[clean_data_df["movie_rating"] > 8]
# print(high_movie_rating_df)

release_data_df = clean_data_df[clean_data_df["movie_release_year"] > 2012]
print(release_data_df)