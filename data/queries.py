from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

def get_top_length_shows():
    return data_manager.execute_select(
        """
        SELECT shows.id, shows.title, COUNT(e.title)* runtime as total_length
        FROM shows
        JOIN seasons s on shows.id = s.show_id
        JOIN episodes e on s.id = e.season_id
        GROUP BY shows.title, runtime, shows.id
        ORDER BY total_length DESC
        LIMIT 10;        
        """
    )

def get_actors_of_show(show):
    return data_manager.execute_select(
        """
        SELECT a.name
        FROM shows
        JOIN show_characters sc on shows.id = sc.show_id
        JOIN actors a on sc.actor_id = a.id
        WHERE shows.id = %{show}s
        ORDER BY a.name;
        """, {'show': show}
    )