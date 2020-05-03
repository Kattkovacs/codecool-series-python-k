from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    season_numbers = queries.season_numbers()
    shows = queries.get_shows()
    if request.args.get('seasons'):
        season_number = request.args.get('seasons')
        seasons_by_number = queries.highest_season_numbers(season_number)
        shows = seasons_by_number
        return render_template('index.html', shows=shows, season_numbers=season_numbers)
    else:
        return render_template('index.html', shows=shows, season_numbers=season_numbers)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


