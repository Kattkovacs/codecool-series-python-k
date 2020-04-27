from flask import Flask, render_template, url_for
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_genres()
    return render_template('index.html', shows=shows)


@app.route('/shows-by-genre/<int:genre_id>', methods=["POST", "GET"])
def shows_by_genre(genre_id):
    shows = queries.get_shows_by_genre(genre_id)
    return render_template('shows.html', shows=shows)



def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


