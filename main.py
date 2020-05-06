from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    min_episode = request.args.get('episode')
    min_seas = request.args.get('season')
    shows = queries.get_min_episode_season(min_episode, min_seas)
    return render_template('design.html', shows=shows)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


