from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artists (name, age) VALUES (%s, %s) RETURNING *"
    values = [artist.name, artist.age]

    results = run_sql(sql, values)
    artist.id = results[0]['id']
    return artist