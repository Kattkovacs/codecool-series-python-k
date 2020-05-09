from data import data_manager


def get_shows_by_year():
    return data_manager.execute_select(
        """
        SELECT date_part('year', shows.year) as show_year 
        FROM shows
        ORDER BY show_year;
        """
    )


def get_actors_by_show_year(year):
    return data_manager.execute_select(
        """
        SELECT actors.name, date_part('year', CURRENT_DATE) - date_part('year', actors.birthday) as age, 
        date_part('year', s.year) as show_year
        FROM actors
        JOIN show_characters sc on actors.id = sc.actor_id
        JOIN shows s on sc.show_id = s.id
        WHERE date_part('year', s.year) = %(year)s and actors.death is null and actors.birthday is not null
        ORDER BY age DESC;
        """, {'year': year}
    )