from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist_1 = Artist("Taylor Swift", 29)
artist_repository.save(artist_1)

album_1 = Album("1989", 2014, artist_1)
album_repository.save(album_1)