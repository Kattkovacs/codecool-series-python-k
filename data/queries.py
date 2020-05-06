from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_min_episode_season(min_episode, min_seas):
    return data_manager.execute_select(
        """
        SELECT shows.id, shows.title, s.season_number, e.episode_number
        FROM shows
        JOIN seasons s on shows.id = s.show_id
        JOIN episodes e on s.id = e.season_id
        GROUP BY shows.id, s.season_number, e.episode_number
        HAVING MIN(s.season_number) >= %(min_seas)s AND MIN(e.episode_number) >= %(min_episode)s;
        """, {'min_episode': min_episode, 'min_seas': min_seas}
    )