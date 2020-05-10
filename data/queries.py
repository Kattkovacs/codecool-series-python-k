from data import data_manager


def get_horror_actors():
    return data_manager.execute_select(
        """
        SELECT s.id, actors.name as actor, actors.birthday, actors.death, g.name
        FROM actors
        JOIN show_characters sc on actors.id = sc.actor_id
        JOIN shows s on sc.show_id = s.id
        JOIN show_genres sg on s.id = sg.show_id
        JOIN genres g on sg.genre_id = g.id
        WHERE g.name = 'Horror';
        """
    )