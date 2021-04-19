import urllib.request, json
import tldextract
from .models import News, Source

apiKey = None
base_url = None


def configure_request(app):
    global apiKey, base_url
    apiKey = app.config["NEWS_API_KEY"]
    base_url = app.config["NEWS_API_BASE_URL"]


def get_source():
    get_sources_url = "https://newsapi.org/v2/sources?apiKey={}".format(apiKey)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url
        get_sources_response = json.load(get_sources_data)
        sources_result = None
        if get_sources_response["sources"]:
            sources_results_list = get_sources_response["sources"]
            sources_results = process_source_results(sources_results_list)

    return sources_results


def get_news():
    get_news_url = base_url.format(apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url
        get_news_response = json.load(get_news_data)
        news_result = None

        if get_news_response["articles"]:
            news_results_list = get_news_response["articles"]
            news_results = process_results(news_results_list)

    return news_results


def search_source(source_name):
    search_news_source_url = "https://newsapi.org/v2/everything?domains={}&sortBy=popularity&apiKey={}".format(
        source_name, apiKey
    )

    with urllib.request.urlopen(search_news_source_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response["articles"]:
            search_news_list = search_news_response["articles"]
            search_news_results = process_results(search_news_list)

    return search_news_results


def process_results(news_list):
    """
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    """
    news_results = []
    for news_item in news_list:
        author = news_item.get("author")
        title = news_item.get("title")
        description = news_item.get("description")
        content = news_item.get("content")
        source_name = news_item.get("source")
        source_url = news_item.get("url")
        source_url_short = tldextract.extract(source_url).registered_domain

        news_object = News(
            author,
            title,
            description,
            content,
            source_name,
            source_url,
            source_url_short,
        )
        news_results.append(news_object)

    return news_results


def process_source_results(news_source_list):
    """
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    """
    source_results = []
    for news_item in news_source_list:
        id = news_item.get("id")
        name = news_item.get("name")
        category = news_item.get("category")
        language = news_item.get("language")
        source_url = news_item.get("url")
        source_url_short = tldextract.extract(source_url).registered_domain

        source_object = Source(
            id, name, category, language, source_url, source_url_short
        )
        source_results.append(source_object)

    return source_results