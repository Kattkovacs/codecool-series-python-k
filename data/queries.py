from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_actors(actor_name_fragment):
    actor_name_fragment = '%' + actor_name_fragment + '%'
    return data_manager.execute_select(
        """
        SELECT actors.name, s.title, sc.character_name
        FROM actors
        JOIN show_characters sc on actors.id = sc.actor_id
        JOIN shows s on sc.show_id = s.id
        WHERE actors.name LIKE %(actor_name_fragment)s
        ORDER BY actors.name
        """, {'actor_name_fragment': actor_name_fragment}
    )