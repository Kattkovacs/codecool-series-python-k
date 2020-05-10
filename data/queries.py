from data import data_manager


def get_4th_episodes():
    return data_manager.execute_select(
        """
            SELECT s2.title, episodes.title as episode, s.season_number, episodes.episode_number
        FROM episodes
            JOIN seasons s on episodes.season_id = s.id
            JOIN shows s2 on s.show_id = s2.id
        WHERE s.season_number = 2
          AND episodes.episode_number = 5
        GROUP BY s2.title, episodes.title, s.season_number, episodes.episode_number;
       """
    )


def get_5th_episodes():
    return data_manager.execute_select(
        """
            SELECT s2.title, episodes.title as episode, s.season_number, episodes.episode_number
        FROM episodes
            JOIN seasons s on episodes.season_id = s.id
            JOIN shows s2 on s.show_id = s2.id
        WHERE s.season_number = 2
          AND episodes.episode_number = 4
        GROUP BY s2.title, episodes.title, s.season_number, episodes.episode_number;
       """
    )
