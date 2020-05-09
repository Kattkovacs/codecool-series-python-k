from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    genres = queries.get_genres()
    genre = request.args.get('genre')
    shows_by_genre = queries.get_shows_by_genre(genre)
    return render_template('index.html', genres=genres, shows_by_genre=shows_by_genre)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


