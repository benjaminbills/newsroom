import unittest
from app.models import News


class NewsTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the News class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_news = News(
            "Kim Hyatt",
            "Burnsville police exchange gunfire with carjacking suspect, who was killed - Minneapolis Star Tribune",
            "Condition of suspect, officers unknown",
            "An armed suspect jumped out of a moving vehicle he",
            "Minneapolis Star Tribune",
            "https://chorus.stimg.co/22453333/08_1012871938_05burn041921.jpg?h=630&w=1200&fit=crop&bg=999&crop=faces",
            '2021-04-19T00:11:15Z"',
            "https://www.startribune.com/burnsville-police-exchange-gunfire-with-carjacking-suspect-who-was-killed/600047474/",
            "www.startribune.com",
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))
