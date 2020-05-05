from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_episodes_sum():
    return data_manager.execute_select(
        """
        SELECT DISTINCT(shows.title), COUNT(e.id) as episode_nums, COUNT(s.id),
        (COUNT(e.id)*COUNT(s.id)) as episodes
        FROM shows
        JOIN seasons s on shows.id = s.show_id
        JOIN episodes e on s.id = e.season_id
        GROUP BY shows.title
        ORDER BY shows.title;
        """
    )