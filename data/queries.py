from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def highest_season_numbers(season_number):
    return data_manager.execute_select(
        """
        SELECT shows.title, COUNT(s.id) as highest_seasons
        FROM shows
        JOIN seasons s on shows.id = s.show_id
        GROUP BY shows.id
        HAVING COUNT(s.id) >= %(season_number)s
        ORDER BY highest_seasons DESC;
        """, {'season_number': season_number}
    )


def season_numbers():
    return data_manager.execute_select(
        """
        SELECT DISTINCT(MAX(s.season_number)) as season_numbers
        FROM seasons as s
        GROUP BY s.id
        ORDER BY season_numbers DESC;
        """
    )

