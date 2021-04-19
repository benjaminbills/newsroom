from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_news, search_source
from ..models import News


@main.route("/")
def index():
    """
    View root page function that returns the index page and its data
    """
    # Getting popular movie
    popular_news = get_news()
    title = "Home - Welcome to The best Movie Review Website Online"

    return render_template("index.html", title=title, popular=popular_news)


@main.route("/search/<source_name>")
def search(source_name):
    """
    View function to display the search results
    """

    searched_news = search_source(source_name)

    title = f"News from {source_name}"
    return render_template("source.html", news_source=searched_news, title=title)
