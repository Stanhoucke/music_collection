import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):
    def setUp(self):
        self.artist_1 = Artist("Taylor Swift", 29)

    def test_artist_has_name(self):
        self.assertEqual("Taylor Swift", self.artist_1.name)

    def test_artist_has_age(self):
        self.assertEqual(29, self.artist_1.age)