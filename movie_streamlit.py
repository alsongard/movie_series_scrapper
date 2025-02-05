import streamlit as st
import pandas as pd
st.write("# YTS.MX MOVIE RATINGS")


data_df = pd.read_csv("./moviescrapper/new_movies.csv")

# st.write(data_df["movie_rating"].dtype)
nan_rows = data_df[data_df.isna().any(axis=1)]
# st.write(f"rows with nan valuesn : {len(nan_rows)} ") # 21

# st.write(nan_rows)

clean_data_df = data_df.dropna()
# clean_data_df

## get maximum values
st.write(f" Highest Rating : {clean_data_df["movie_rating"].max()} ")
st.write(f" Lowest Rating : {clean_data_df["movie_rating"].min()}")

# get top movies
st.write("TOP BEST MOVIES")
best_movies_df = clean_data_df[clean_data_df["movie_rating"] > 8]
best_movies_df


# check the number of  ratings for each rate using value_counts
st.write(clean_data_df["movie_rating"].value_counts())



movie_category = input("Enter category of movie you would want: ")