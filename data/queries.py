# o03
# Írassuk ki az összes műfajt, átlagolt rating alapján rendezzük sorba.
# JS - ha a ratingre kattintasz, felugró ablakban jelenjen meg a hozzá tartozó genre.


from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_genres_rating():
    return data_manager.execute_select(
        """
                SELECT genres.name, AVG(ROUND(s.rating, 2))
        FROM genres
                 JOIN show_genres sg on genres.id = sg.genre_id
                 JOIN shows s on sg.show_id = s.id
        GROUP BY genres.name, s.rating
        ORDER BY AVG(ROUND(s.rating, 2));
        """
    )
