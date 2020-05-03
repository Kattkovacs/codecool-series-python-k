from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

def get_genres():
    return data_manager.execute_select(
        """
        SELECT genres.name
        FROM genres
        ORDER BY genres.name;
        """
    )

def shows_by_genre():
    return data_manager.execute_select(

    )

