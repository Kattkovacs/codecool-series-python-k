from data import data_manager


def get_genres_by_death_actors():
    return data_manager.execute_select(
        """
                SELECT DISTINCT(g.name) as genre
        FROM actors
                 JOIN show_characters sc on actors.id = sc.actor_id
                 JOIN shows s on sc.show_id = s.id
                 JOIN show_genres sg on s.id = sg.show_id
                 JOIN genres g on sg.genre_id = g.id
        WHERE actors.death is not null;
        """
    )



def get_actors(genre):
    return data_manager.execute_select(
        """
         SELECT actors.name, g.name as genre,
           date_part('year', actors.death) - date_part('year', actors.birthday) as age
        FROM actors
                 JOIN show_characters sc on actors.id = sc.actor_id
                 JOIN shows s on sc.show_id = s.id
                 JOIN show_genres sg on s.id = sg.show_id
                 JOIN genres g on sg.genre_id = g.id
        WHERE actors.death is not null AND g.name = %(genre)s
        ORDER BY age DESC;
        """, {'genre': genre}
    )