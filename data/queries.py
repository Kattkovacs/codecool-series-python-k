from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_actors_by_date(search):
    return data_manager.execute_select(
        """
        SELECT actors.id, actors.name, actors.birthday as date, COUNT(sc.character_name), AVG(s.rating)
        FROM actors
        JOIN show_characters sc on actors.id = sc.actor_id
        JOIN shows s on sc.show_id = s.id
        WHERE actors.birthday <= %(search)s
        GROUP BY actors.id, actors.name, actors.birthday;
        """,  {'search': search}
    )
