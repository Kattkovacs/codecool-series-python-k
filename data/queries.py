from data import data_manager


# def get_shows():
#     return data_manager.execute_select('SELECT id, title FROM shows;')

def get_actor_cards():
    return data_manager.execute_select(
        """
        SELECT actors.name,
       CASE
            WHEN actors.death is null THEN date_part('year', CURRENT_DATE) - date_part('year',actors.birthday)
            WHEN actors.death is not null THEN date_part('year', actors.death) - date_part('year', actors.birthday)
            
        END as age,
       COUNT(s.id),
        CASE
            WHEN actors.death is not null THEN 'dead'
            WHEN actors.death is null THEN 'alive'
        END as dead_alive
        FROM actors
        JOIN show_characters sc on actors.id = sc.actor_id
        JOIN shows s on sc.show_id = s.id
        GROUP BY actors.name, actors.birthday, actors.death
        ORDER BY COUNT(s.id) DESC;
        """
    )
