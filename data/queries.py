from data import data_manager


def get_shows():
    return data_manager.execute_select(
        """
        SELECT id, title, date_part('year', CAST(shows.year AS DATE)) as year FROM shows;
        """)


def get_shows_by_given_year(year):
    return data_manager.execute_select(
        """
        SELECT a.name, (date_part('year', CAST(shows.year AS DATE)) - date_part('year', a.birthday)) as age, 
        to_char(date_part('year', shows.year)) as year
        FROM shows
        JOIN show_characters sc on shows.id = sc.show_id
        JOIN actors a on sc.actor_id = a.id
        GROUP BY a.name, age, shows.year
        HAVING year = %(year)s
        ORDER BY age ASC;
        """, {'year': year}
    )