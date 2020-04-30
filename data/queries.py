from data import data_manager


def get_shows():
    return data_manager.execute_select(
        """
                SELECT shows.id, shows.title, g.name as genres, COUNT(sc.id) as characters
        FROM shows
        JOIN show_genres sg on shows.id = sg.show_id
        JOIN genres g on sg.genre_id = g.id
        JOIN show_characters sc on shows.id = sc.show_id
        GROUP BY shows.id, shows.title, g.name
        """
    )


def get_shows_by_genre(genre):
    return data_manager.execute_select(
        """
        SELECT shows.id, shows.title, g.name as genres, COUNT(sc.id) as characters
        FROM shows
        JOIN show_genres sg on shows.id = sg.show_id
        JOIN genres g on sg.genre_id = g.id
        JOIN show_characters sc on shows.id = sc.show_id
        GROUP BY shows.id, shows.title, g.name
        HAVING genres = %{genre}s;
        """, {'genre': genre}
    )
