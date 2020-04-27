from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

def get_show_by_title(search):
    return data_manager.execute_select(
        """
        SELECT *
        FROM shows
        WHERE LOWER(title) LIKE LOWER(%(search)s)
        ORDER BY id;
        """, {'search': search}
    )