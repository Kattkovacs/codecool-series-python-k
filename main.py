from datetime import datetime

from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows_by_year()
    return render_template('index.html', shows=shows)


@app.route('/actors-by-age')
def actors_by_show_age():
    year = request.args.get('year')
    actors = queries.get_actors_by_show_year(year)
    for actor in actors:
        show_age = datetime.now().year - actor['show_year']
        if show_age > actor['age']:
            actor['older'] = 'younger'
        else:
            actor['older'] = 'older'
    return render_template('design.html', actors=actors, year=year, show_age=show_age)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


