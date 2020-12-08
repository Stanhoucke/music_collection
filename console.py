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

# print(artist_repository.select(16).__dict__)

# res = artist_repository.select_all()
# for artist in res:
#     print(artist.__dict__)

# update_artist_1 = Artist("Taylor Swift", 30, artist_1.id)
# artist_repository.update(update_artist_1)

# Albums
album_1 = Album("1989", 2014, artist_1)
album_repository.save(album_1)
album_2 = Album("Because the Internet", 2013, artist_2)
album_repository.save(album_2)
album_3 = Album("Awaken, My Love!", 2016, artist_2)
album_repository.save(album_3)

# print(album_repository.select(31).__dict__)

# res = album_repository.select_all()
# for album in res:
#     print(album.__dict__)

# res = album_repository.select_by_artist(artist_2)
# for album in res:
#     print(album.__dict__)

# update_album_1 = Album("1989", 2015, artist_1, album_1.id)
# album_repository.update(update_album_1)

album_repository.delete(album_1)
artist_repository.delete(artist_1)