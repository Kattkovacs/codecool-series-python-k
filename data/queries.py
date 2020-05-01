from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_character_details(search):
    return data_manager.execute_select(
        """
        SELECT show_characters.character_name as char, s.title, a.name
        FROM show_characters
        JOIN actors a on show_characters.actor_id = a.id
        JOIN shows s on show_characters.show_id = s.id
        GROUP BY show_characters.character_name, show_characters.id, s.id, s.title, a.id, a.name
        HAVING LOWER(show_characters.character_name) LIKE LOWER(%(search)s)
        """, {'search': search}
    )