
# táblázat
# sorozat neve, mennyi actor death szereplő legtöbb halott legyen felül
# urlben menjen egy szám
# amely azalsó limit a halottak számára
# 2 oszlop 1 sorozat neve/halottak száma
# JS a sorozat címére, vagy a halottak száma fölé vitt egérrel a mező random színűre változzon

from data import data_manager


def get_shows_by_deaths(deaths_number):
    return data_manager.execute_select(
        """
        SELECT shows.title, COUNT(a.death) as deaths
        FROM shows
                 JOIN show_characters sc on shows.id = sc.show_id
                 JOIN actors a on sc.actor_id = a.id
        GROUP BY shows.title
        HAVING COUNT(a.death) > %(deaths_number)s
        ORDER BY deaths DESC;
        """, {'deaths_number': deaths_number}
    )
