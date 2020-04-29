from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

def get_selected_shows():
    return data_manager.execute_select(
        """
        SELECT shows.title, COUNT(e.id)
FROM shows
         JOIN seasons s on shows.id = s.show_id
         JOIN episodes e on s.id = e.season_id
GROUP BY shows.title
HAVING COUNT(e.id) < ((
                          SELECT COUNT(e.id)
                          FROM episodes as e
                      ) / COUNT(shows.id));
        """
    )