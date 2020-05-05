from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_query_by_selection(selected_type, order):
    return data_manager.execute_select(
        """
        SELECT
    shows.title as shows, s.title as seasons, e.title as episodes
FROM shows
         JOIN seasons s on shows.id = s.show_id
         JOIN episodes e on s.id = e.season_id
GROUP BY shows.title, s.title, e.title
ORDER BY
            CASE WHEN %(selected_type)s ='shows' AND %(order)s = 'ASC' THEN shows.title END,
        CASE WHEN %(selected_type)s ='shows' AND %(order)s = 'DESC' THEN shows.title END DESC,
        CASE WHEN %(selected_type)s ='seasons' AND %(order)s = 'ASC' THEN  s.title END,
        CASE WHEN %(selected_type)s ='seasons' AND %(order)s = 'DESC' THEN shows.title END DESC,
        CASE WHEN %(selected_type)s ='episodes' AND %(order)s = 'ASC' THEN  e.title END,
        CASE WHEN %(selected_type)s ='episodes' AND %(order)s = 'DESC' THEN shows.title END DESC
        LIMIT 50;

        """, {'selected_type': selected_type, 'order': order}

    )