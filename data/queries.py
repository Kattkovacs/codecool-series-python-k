from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

def get_genre_tops(genre):
    return data_manager.execute_select(
        """SELECT shows.title,
            shows.year,
            ROUND(shows.rating,1) AS rating
            FROM shows
            JOIN show_genres sg ON shows.id = sg.show_id
            JOIN genres g ON sg.genre_id = g.id
            WHERE g.name = %(genre)s
            GROUP BY shows.title, shows.year, rating
            ORDER BY rating DESC
            LIMIT 10;
    """, {"genre": genre}
    )