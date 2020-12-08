import unittest
from models.album import Album
from models.artist import Artist

class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.artist_1 = Artist("Taylor Swift", 29)
        self.album_1 = Album("1989", 2014, self.artist_1)