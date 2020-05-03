from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def highest_season_numbers(season_number):
    return data_manager.execute_select(
        """
        SELECT shows.title, MAX(s.season_number) as highest_seasons
        FROM shows
        JOIN seasons s on shows.id = s.show_id
        GROUP BY shows.title, s.season_number
        HAVING s.season_number >= %(season_number)s
        ORDER BY highest_seasons DESC;
        """, {'season_number': season_number}
    )



def season_numbers():
    return data_manager.execute_select(
        """
        SELECT MAX(s.season_number) as season_numbers
        FROM seasons as s
        GROUP BY s.season_number
        ORDER BY season_numbers DESC;
        """
    )

