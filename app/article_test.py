import unittest
from models import article
Article = article.Artcle


class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles= Article('PayPal to let you buy and sell cryptocurrencies in the US','Ritha','A thrilling new Python Series','2020-10-21T13:28:15Z','http://techcrunch.com/2020/10/21/paypal-to-let-you-buy-and-sell-cryptocurrencies-in-the-us/','https://image.tmdb.org/t/p/w500/khsjha27hbs')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Article))


if __name__ == '__main__':
    unittest.main()