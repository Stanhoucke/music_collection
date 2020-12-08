from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album
import repositories.album_repository as album_repository

def save(artist):
    sql = "INSERT INTO artists (name, age) VALUES (%s, %s) RETURNING *"
    values = [artist.name, artist.age]

    results = run_sql(sql, values)
    artist.id = results[0]['id']
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['name'], result['age'], result['id'])
    return artist

def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    result = run_sql(sql)

    for row in result:
        artist = Artist(row['name'], row['age'], row['id'])
        artists.append(artist)
    return artists

def update(artist):
    sql = "UPDATE artists SET (name, age) = (%s, %s) WHERE id = %s"
    values = [artist.name, artist.age, artist.id]
    run_sql(sql, values)

def delete(artist):
    artist_albums = album_repository.select_by_artist(artist)
    for album in artist_albums:
        sql = "UPDATE albums SET artist_id = NULL WHERE id = %s"
        values = [album.id]
        run_sql(sql, values)

    sql = "DELETE FROM artists WHERE id = %s"
    values =[artist.id]
    run_sql(sql, values)