from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_genres():
    return data_manager.execute_select(
        """
        SELECT genres.id, genres.name, COUNT(sg.show_id) as count
        FROM genres
        JOIN show_genres sg on genres.id=sg.genre_id
        GROUP BY genres.name, genres.id
        ORDER BY genres.name;
        """
    )


def get_shows_by_genre(id):
    return data_manager.execute_select(
        """
        SELECT s.title, s.year
        FROM shows s 
        JOIN show_genres sg on s.id = sg.show_id
        WHERE sg.genre_id = %(genre_id)s
        ORDER BY s.title;
        """, {'genre_id': id}
    )