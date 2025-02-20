import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

st.logo(
    image="https://yts.mx/assets/images/website/logo-YTS.svg",
    size="large"
)
st.sidebar.write("YTS.MX scrapper analyzer")
user_options = ["year", "category"]
entered_option = st.sidebar.selectbox("Select movie based on :", user_options)
st.write("### YTS.MX MOVIES")


data_df = pd.read_csv("./moviescrapper/data/all_movie_data.csv")

# st.write("data_df from /moviescrapper/data/all_movie_data.csv")
data_df.drop(data_df.columns[data_df.columns.str.contains('Unnamed')], axis=1, inplace=True) # drop Unnamed column
# data_df

# get data from previous file:
get_new_data_daily_df = pd.read_csv("./moviescrapper/data/all_movie_data.csv")
# st.write("Getting data from /moviescrapper/data/all_movie_data.csv")
get_new_data_daily_df.drop(get_new_data_daily_df.columns[get_new_data_daily_df.columns.str.contains("Unnamed")], axis=1, inplace=True)
# get_new_data_daily_df


# combine database
new_data_df = pd.concat([get_new_data_daily_df, data_df], ignore_index=True) # for ultimate_backup_file
# new_data_df

# st.write("NEW_DATA_DF")
# new_data_df = new_data_df.drop("Unnamed", axis=0)
# new_data_df.columns
# st.write(data_df["movie_rating"].dtype)

nan_rows = new_data_df[new_data_df.isna().any(axis=1)]
# st.write(f"rows with nan valuesn : {len(nan_rows)} ") # 53

## CLEAN DATAFRAME
clean_data_df = new_data_df.dropna()
# clean_data_df.to_csv("./moviescrapper/data/all_movie_data.csv") added data to ultime_backup_file
## GET NUMBER OF DUPLICATES
duplicated = clean_data_df.duplicated().value_counts()

clean_data_df = clean_data_df.drop_duplicates()



# check datatypes
# column_data_types = clean_data_df.dtypes
# column_data_types


## get maximum values
highest_rating = clean_data_df["movie_rating"].max()
lowest_rating = clean_data_df["movie_rating"].min()

st.text(f"""Movie Ratings \n \t Highest Rating: {highest_rating} \n \t Lowest Rating: {lowest_rating}""")

# check the number of  ratings for each rate using value_counts
# st.write(clean_data_df["movie_rating"].value_counts())

movie_categories = ["Action", "Drama", "Comedy", "Horror", "Adventure", "Crime", "Sci-Fi", "Documentary"]
if entered_option == "year":
    movie_data_year_based_df = clean_data_df.sort_values(by=["movie_release_year"], ascending=False).reset_index(drop=True)
    movie_data_year_based_df

else:
    category_entered = st.sidebar.selectbox("Select the category of the movie you wish to view:", movie_categories)
    movie_data_category_based_df = clean_data_df[clean_data_df["movie_category"] == category_entered].reset_index(drop=True)
    
    yes_no_options = ["yes", "no"]
    two_option_answer = st.sidebar.selectbox(f"Get movies with highest rating in {category_entered}", yes_no_options)

    if two_option_answer == "yes":
        movie_data_category_sorted_based_df = movie_data_category_based_df.sort_values(by=["movie_rating"], ascending=False).reset_index(drop=True)
        movie_data_category_sorted_based_df
    else:
        movie_data_category_based_df