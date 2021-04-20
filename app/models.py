class News:
    """
    News class to define News Objects
    """

    def __init__(
        self,
        author,
        title,
        description,
        content,
        source_name,
        urlToImage,
        publishedAt,
        source_url,
        source_url_short,
    ):
        self.author = author
        self.title = title
        self.description = description
        self.content = content
        self.source_name = source_name
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.source_url = source_url
        self.source_url_short = source_url_short


class Source:
    """
    Source class to define Source Objects
    """

    def __init__(self, id, name, category, language, source_url, source_url_short):
        self.id = id
        self.name = name
        self.category = category
        self.language = language
        self.source_url = source_url
        self.source_url_short = source_url_short
