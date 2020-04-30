from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

def get_years():
    return data_manager.execute_select(
        """
        SELECT date_part('year', year) as year, ROUND(AVG(rating),1) as average, COUNT(id)
        FROM shows
        WHERE date_part('year', year) >= 1970 and date_part('year', year) <= 2010
        GROUP BY year;
        """
    )