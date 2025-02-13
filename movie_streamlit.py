import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
st.write("# YTS.MX MOVIE RATINGS")


data_df = pd.read_csv("./moviescrapper/new_movies.csv")

# st.write(data_df["movie_rating"].dtype)
nan_rows = data_df[data_df.isna().any(axis=1)]
# st.write(f"rows with nan valuesn : {len(nan_rows)} ") # 21

# st.write(nan_rows)

clean_data_df = data_df.dropna()
# clean_data_df

## get maximum values
highest_rating = clean_data_df["movie_rating"].max()
lowest_rating = clean_data_df["movie_rating"].min()

st.text(f"""Movie Ratings \n \t Highest Rating: {highest_rating} \n \t Lowest Rating: {lowest_rating}""")

# check the number of  ratings for each rate using value_counts
# st.write(clean_data_df["movie_rating"].value_counts())


# get top movies
st.write("TOP BEST MOVIES WITH  RATINGS OF 8 AND ABOVE")
best_movies_df = clean_data_df[clean_data_df["movie_rating"] >= 8].reset_index(drop=True)
# best_movies_df
best_movies_df = best_movies_df.sort_values(by=["movie_rating"], ascending=False).reset_index(drop=True)
best_movies_df
# print(type(best_movies_df))
# st.write("Top Movie Category based on best movies with ratings higher than 8")
st.write("The chart belows shows the which movie category has the highest number of movies with high ratings.")
# st.write(best_movies_df["movie_category"].value_counts())

best_movies_category_ratings = best_movies_df["movie_category"].value_counts().rename_axis('movie_category').reset_index(name="count")
st.bar_chart(best_movies_category_ratings,x="movie_category", x_label="Highest Number of Movies", y_label="Movie Category", horizontal=True)
best_movies_category_ratings
st.write("You have 8 movies in the category ACTION that have a rating of above 8")


## MOVIE RATINGS FROM 5 TO 7.9
st.write("# Movie ratings from 5 to 7.9")
mid_range_movies_df = clean_data_df[clean_data_df["movie_rating"].between(5, 7.9)].reset_index(drop=True)
# mid_range_movies_df
# check datatype of movie_release_year
# st.text(f"Data type of column movie_release_year is {mid_range_movies_df[""]}")
mid_range_movies_sorted_df = mid_range_movies_df.sort_values(by=["movie_rating"],ascending=False)
mid_range_movies_sorted_df

st.write("The chart belows shows the which movie category has the highest number of movies with high ratings.")
mid_range_category_ratings = mid_range_movies_sorted_df["movie_category"].value_counts().rename_axis('movie_category').reset_index(name="count")
mid_range_category_ratings
st.bar_chart(mid_range_category_ratings,x="movie_category", x_label="Highest Number of Movies", y_label="Movie Category", horizontal=True)
