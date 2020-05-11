from data import data_manager


def get_actors_with_genres():
    return data_manager.execute_select(
        """
        SELECT actors.name, string_agg(g.name, ', ') as genre
        FROM actors
        JOIN show_characters sc on actors.id = sc.actor_id
        JOIN shows s on sc.show_id = s.id
        JOIN show_genres sg on s.id = sg.show_id
        JOIN genres g on sg.genre_id = g.id
        GROUP BY actors.name
        ORDER BY actors.name ASC;
        """
    )
