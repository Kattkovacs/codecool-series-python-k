from data import data_manager


def get_shows():
    return data_manager.execute_select(
        """
        SELECT actors.name
        FROM actors
        WHERE LOWER(LEFT(actors.name, 1)) = 'a' OR actors.name LIKE '% A%'
        ORDER BY actors.name DESC;
"""
    )
