from data import data_manager


def get_shows():
    return data_manager.execute_select(
        """
        SELECT DISTINCT(date_part('year', shows.year)) as s_year
        FROM shows
        ORDER BY s_year DESC;
        """)


def get_shows_by_given_year(year):
    return data_manager.execute_select(
        """
            SELECT a.name, date_part('year', shows.year) as s_year, a.death, a.birthday,
            CASE
            WHEN a.death IS NULL AND a.birthday IS NOT NULL THEN (date_part('year', CAST(shows.year AS DATE)) - date_part('year', a.birthday))
            WHEN a.death IS NOT NULL AND a.birthday IS NULL THEN (date_part('year', a.death) - date_part('year', a.birthday))
            ELSE 0000
            END as age
            FROM shows
                     JOIN show_characters sc on shows.id = sc.show_id
                     JOIN actors a on sc.actor_id = a.id
            GROUP BY a.name, s_year, a.death, a.birthday
            HAVING date_part('year', shows.year) = %(year)s
            ORDER BY age DESC;        
        """, {'year': year}
    )