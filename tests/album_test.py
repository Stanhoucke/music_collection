import unittest
from models.album import Album
from models.artist import Artist

class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.artist_1 = Artist("Taylor Swift", 29)
        self.album_1 = Album("1989", 2014, self.artist_1)

    def test_album_has_title(self):
        self.assertEqual("1989", self.album_1.title)

    def test_album_has_year(self):
        self.assertEqual(2014, self.album_1.year)

    def test_album_has_artist(self):
        self.assertEqual(self.artist_1, self.album_1.artist)
