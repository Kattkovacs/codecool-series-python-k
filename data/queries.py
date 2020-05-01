from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_actors_by_title():
    return data_manager.execute_select(
        """
SELECT actors.id, actors.name,
       (date_part('year', current_date) - date_part('year', actors.birthday)) AS age,
       (date_part('year', actors.death) - date_part('year', actors.birthday)) AS death_age,
       COUNT(s.title) AS number_of_shows, actors.death,
       CASE
            WHEN actors.death IS NOT NULL THEN 'dead'
            ELSE 'alive'
        END AS status
FROM actors
         JOIN show_characters sc on actors.id = sc.actor_id
         JOIN shows s on sc.show_id = s.id

GROUP BY actors.id, actors.name
ORDER BY number_of_shows DESC;
        """
    )