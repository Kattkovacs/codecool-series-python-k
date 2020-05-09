from flask import Flask, render_template, url_for
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    max_season = queries.get_max_season()
    shows = queries.get_shows_by_season_number()
    return render_template('index.html', shows=shows, max_season=max_season)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


