from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_actors_by_character():
    return data_manager.execute_select(
        """
        SELECT actors.name as actor, COUNT(sc.character_name) as played_characters
        FROM actors
        JOIN show_characters sc on actors.id = sc.actor_id
        GROUP BY actors.name, sc.character_name
        ORDER BY COUNT(sc.character_name) DESC
        LIMIT 10;
        """
    )