from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_max_season():
    return data_manager.execute_select(
        """
        SELECT DISTINCT(MAX(seasons.season_number))
        FROM seasons;
        """
    )


def get_shows_by_season_number():
    return data_manager.execute_select(
        """
        SELECT shows.id, shows.title, COUNT(s.season_number)
        FROM shows
        JOIN seasons s on shows.id = s.show_id
        GROUP BY shows.id, shows.title;
        """
    )