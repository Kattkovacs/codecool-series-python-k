from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_shows_by_year():
    return data_manager.execute_select(
        """
        SELECT date_part('year', year) as year, ROUND(AVG(rating), 1) as average_rating, COUNT(id)
        FROM shows
        GROUP BY year
        HAVING date_part('year', year) < 2010 and 1970 < date_part('year', year)
        ORDER BY year
        ;
        """
    )
