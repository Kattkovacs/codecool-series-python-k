from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_to_runtime_shows():
    return data_manager.execute_select(
        """
        SELECT shows.title, shows.id, shows.runtime*COUNT(e.id) as runtime
        FROM shows
        JOIN seasons s on shows.id = s.show_id
        JOIN episodes e on s.id = e.season_id
        GROUP BY shows.title,  shows.id, runtime
        ORDER BY runtime DESC
        LIMIT 10;
        """
    )


def get_actors(id):
    return data_manager.execute_select(
        """
        SELECT a.name as actors
        FROM shows
        JOIN show_characters sc on %(show_id)s = sc.show_id
        JOIN actors a on sc.actor_id = a.id
        GROUP BY a.name
        ORDER BY a.name DESC;
        """, {'show_id': id}
    )