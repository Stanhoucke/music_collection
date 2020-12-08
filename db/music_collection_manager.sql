DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    year INT,
    artist_id INT REFERENCES artists(id)
);


-- UPDATE albums SET (title, year, artist_id) = ('1989', 2015, 1) WHERE id = 1;
