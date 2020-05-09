from data import data_manager


def get_genres():
    return data_manager.execute_select('SELECT genres.name FROM genres;')


def get_shows_by_genre(genre):
    return data_manager.execute_select(
        """
        SELECT shows.title, shows.year, ROUND(shows.rating, 1), g.name as genre
        FROM shows
        JOIN show_genres sg on shows.id = sg.show_id
        JOIN genres g on sg.genre_id = g.id
            WHERE g.name = %(genre)s
        ORDER BY shows.rating DESC
        LIMIT 10;
    """, {'genre': genre}

    )
