from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_titles(num):
    return data_manager.execute_select(
        """
        SELECT shows.title, COUNT(genre_id) as numbers_of_genres
        FROM shows
        JOIN show_genres sg on shows.id = sg.show_id
        JOIN genres g on sg.genre_id = g.id
        GROUP BY shows.title
        HAVING COUNT(genre_id)>=%(num)s;
        """, {'num': num}
    )