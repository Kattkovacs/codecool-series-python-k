from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_query_by_selection(selected_type, order):
    return data_manager.execute_select(
        """
        SELECT shows.title as shows, s.title as seasons, e.title as episodes
        FROM shows
        JOIN seasons s on shows.id = s.show_id
        JOIN episodes e on s.id = e.season_id
        GROUP BY shows.title, s.title, e.title
        ORDER BY 
        CASE WHEN %(order)s = 'ASC' THEN %(selected_type)s END ASC,
        CASE WHEN %(order)s = 'DESC' THEN %(selected_type)s END DESC
        LIMIT 50;
        """, {'selected_type': selected_type, 'order': order}

    )