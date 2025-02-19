# YTS MOVIE SCRAPPER AND ANALYZER USING STREAMLIT

[![wakatime](https://wakatime.com/badge/user/ca37100b-7f0f-4ae1-947c-ff595165e688/project/08ce1bb1-8e14-4eda-830c-a0dbd259b83b.svg)](https://wakatime.com/badge/user/ca37100b-7f0f-4ae1-947c-ff595165e688/project/08ce1bb1-8e14-4eda-830c-a0dbd259b83b)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/moviescrapper.git
    cd moviescrapper
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the root directory and add your [SCRAPEOPS_API_KEY](http://_vscodecontentref_/10):
    ```env
    SCRAPEOPS_API_KEY=your_api_key_here
    ```

## Usage

1. Run the Scrapy spider to scrape movie data:
    ```sh
    scrapy crawl moviespider
    ```

2. After scraping, the data will be saved in [movieData.csv](http://_vscodecontentref_/11). You can analyze this data using Python.

3. To visualize the data using Streamlit, run:
    ```sh
    streamlit run app.py
    ```

## Files

- [scrapy.cfg](http://_vscodecontentref_/12): Scrapy configuration file.
- [items.py](http://_vscodecontentref_/13): Defines the models for the scraped items.
- [middlewares.py](http://_vscodecontentref_/14): Contains custom middleware for the project.
- [pipelines.py](http://_vscodecontentref_/15): Processes the scraped items.
- [settings.py](http://_vscodecontentref_/16): Scrapy settings for the project.
- [moviespider.py](http://_vscodecontentref_/17): The spider that scrapes movie data from YTS.
- [movieData.csv](http://_vscodecontentref_/18): The CSV file where the scraped movie data is stored.
- [new_movies.csv](http://_vscodecontentref_/19): Additional movie data for analysis.

## Streamlit App

The Streamlit app provides a user-friendly interface to visualize and analyze the scraped movie data. It includes features such as:

- Displaying movie details
- Filtering movies by category, rating, and release year
- Visualizing data trends and distributions

[streamlit-movie_streamlit-2025-02-13-03-02-43.webm](https://github.com/user-attachments/assets/0e6be360-a233-4c94-9120-306c3dd3378e)


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Scrapy](https://scrapy.org/)
- [Streamlit](https://streamlit.io/)
- [YTS](https://yts.mx/)
