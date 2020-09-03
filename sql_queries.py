# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays(
    songplay_id SERIAL PRIMARY KEY,
    start_time timestamp NOT NULL REFERENCES time(start_time),
    user_id integer NOT NULL REFERENCES users(user_id),
    level varchar,
    song_id varchar REFERENCES songs(song_id),
    artist_id varchar REFERENCES artists(artist_id),
    session_id integer,
    location varchar,
    user_agent varchar
    )
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users(
    user_id integer PRIMARY KEY,
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar,
    time_stamp timestamp
    )
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs(
    song_id varchar PRIMARY KEY,
    title varchar,
    artist_id varchar,
    year integer,
    duration numeric
    )
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists(
    artist_id varchar PRIMARY KEY,
    name varchar,
    location varchar,
    latitude numeric,
    longitude numeric
    )
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time(
    start_time timestamp PRIMARY KEY,
    hour smallint,
    day smallint,
    week smallint,
    month smallint,
    year smallint,
    weekday int
    )
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
""")

user_table_insert = ("""
    INSERT INTO users(user_id, first_name, last_name, gender, level, time_stamp)
    VALUES(%s,%s,%s,%s,%s,%s) ON CONFLICT (user_id) DO UPDATE SET level=( CASE WHEN users.time_stamp > EXCLUDED.time_stamp THEN users.level ELSE EXCLUDED.level END);
""")

song_table_insert = ("""
    INSERT INTO songs(song_id,title,artist_id,year,duration)
    VALUES(%s,%s,%s,%s,%s) ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artists(artist_id, name, location, latitude, longitude)
    VALUES(%s,%s,%s,%s,%s) ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
    INSERT INTO time(start_time, hour, day, week, month, year, weekday)
    VALUES(%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT song_id, songs.artist_id
    from songs
    join artists
    on songs.artist_id=artists.artist_id
    where songs.title=%s and artists.name=%s and songs.duration=%s
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]