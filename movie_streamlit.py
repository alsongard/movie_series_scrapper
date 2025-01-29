import streamlit as st
import pandas as pd
st.write("# YTS.MX MOVIE RATINGS")

st.write("best movies")

data_df = pd.read_csv("./moviescrapper/moviescrapper/movieData.csv")

data_df

# st.write(data_df["movie_rating"].dtype)
nan_rows = data_df[data_df.isna().any(axis=1)]
st.write(nan_rows)

clean_data_df = data_df.dropna()
clean_data_df


clean_data_df["movie_rating"] = clean_data_df["movie_rating"].astype(str)

clean_data_df["movie_rating"] = clean_data_df["movie_rating"].apply(lambda rating : rating.replace("/10", ""))

st.write("movie_rating new datatype")
clean_data_df