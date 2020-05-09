from data import data_manager


# def get_birth_years():
#     return data_manager.execute_select(
#         """
#         SELECT date_part('year', actors.birthday) FROM actors;
#         """
#     )


def get_actors_by_year(year):
    return data_manager.execute_select(
        """
        SELECT actors.name, actors.birthday, COUNT(sc.id) as played_characters,
                ROUND(AVG(s.rating),1) as average_rating
        FROM actors
        JOIN show_characters sc on actors.id = sc.actor_id
        JOIN shows s on sc.show_id = s.id
        GROUP BY actors.name, actors.birthday
        HAVING date_part('year', actors.birthday) >= %(year)s
        ;
        """, {'year': year}
    )