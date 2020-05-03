from flask import Flask, render_template, url_for
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    genres = queries.get_genres()
    print(genres)
    return render_template('design.html', genres=genres)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


