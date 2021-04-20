import unittest
from app.models import Source


class NewsSourceTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Source class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.news_source = Source(
            "abc-news",
            "ABC News",
            "general",
            "en",
            "http://www.abc.net.au/news",
            "abc.net.au",
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.news_source, Source))
