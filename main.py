from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    if request.args.get('genre'):
        genre = request.args.get('genre')
        return render_template('design.html', genre=genre)
    genres_by_actors = queries.get_genres_by_death_actors()
    return render_template('index.html', genres_by_actors=genres_by_actors)


@app.route('/design/<genre>', methods=['GET'])
def design():
    actors = queries.get_actors(genre)
    return render_template('design.html', actors=actors)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


