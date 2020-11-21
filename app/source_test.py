import unittest
from sources import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_sources= Sources('general','IGIHE','Amakuru ashyushye wayasanga ku Igihe','https://image.tmdb.org/t/p/w500/khsjha27hbs')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,Sources))


if __name__ == '__main__':
    unittest.main()