from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_news, get_source, search_source
from ..models import News


@main.route("/")
def index():
    """
    View root page function that returns the index page and its data
    """
    # Getting top headlines
    news_source = get_source()

    top_headlines = get_news()
    title = "Home - Welcome to The best Movie Review Website Online"

    return render_template(
        "index.html", title=title, popular=top_headlines, source=news_source
    )


@main.route("/search/<source_name>")
def search(source_name):
    """
    View function to display the search source
    """

    searched_news = search_source(source_name)
    if searched_news:

        title = f"News from {source_name}"
        return render_template("source.html", news_source=searched_news, title=title)
    else:
        title = f"No News from {source_name}"
        return render_template("no_news.html", title=title)
