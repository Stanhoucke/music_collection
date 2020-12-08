from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (title, year, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.year, album.artist.id]

    results = run_sql(sql, values)
    album.id = results[0]['id']
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)
