from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

# Artists
artist_1 = Artist("Taylor Swift", 29)
artist_repository.save(artist_1)
artist_2 = Artist("Childish Gambino", 37)
artist_repository.save(artist_2)

# Albums
album_1 = Album("1989", 2014, artist_1)
album_repository.save(album_1)
album_2 = Album("Because the Internet", 2013, artist_2)
album_repository.save(album_2)
album_3 = Album("Awaken, My Love!", 2016, artist_2)
album_repository.save(album_3)