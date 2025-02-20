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


st.write("""
    movie categories are:
    1. Action
    2. Drama
    3. Comedy
    4. Horror
    5. Adventure
    6. Crime
    7. Sci-Fi
    8. Documentary

""")
movie_category = st.text_input("From the above movie categories , enter a the movie category number for which you wish to view the best movie ratings in that category: ")
# st.text(f"data type of st.text_input is {type(movie_category)}")  input data is string datatype

movie_result = ""

match movie_category:
    case "1":
        movie_result = "Action"
    case "2":
        movie_result = "Drama"
    case "3":
        movie_result = "Comedy"
    case "4": 
        movie_result = "Horror"
    case "5":
        movie_result = "Adventure"
    case "6":
        movie_result = "Crime"
    case "7":
        movie_result = "Sci-Fi"
    case "8":
        movie_result = "Documentary"
    case _:
        movie_result = False

# st.text(f"Movie category entered is {movie_result}")

if movie_result == False:
    st.write("Select an appropriate movie category number")
else:
    st.text(f"Displaying movies that are categorized under {movie_result}")
    action_movie_df = clean_data_df[clean_data_df["movie_category"] == movie_result]
    action_movie_df = action_movie_df.sort_values(by="movie_rating", ascending=False).reset_index(drop=True)
    action_movie_df