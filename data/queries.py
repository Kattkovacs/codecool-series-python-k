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
        LIMIT 10;

        """, {'selected_type': selected_type, 'order': order}

    )


def get_overviews(selected_type):
    return data_manager.execute_select(
        """
        SELECT 
        shows.overview as shows, s.overview as seasons, e.overview as episodes
        FROM shows
        JOIN seasons s on shows.id = s.show_id
        JOIN episodes e on s.id = e.season_id
        GROUP BY shows.overview, s.overview, e.overview
        LIMIT 10;
        """, {'selected_type': selected_type}
    )