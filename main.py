from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design', methods=["POST", "GET"])
def design():
    if request.method == "POST":
        genre = request.form('genre')
        shows = queries.get_shows_by_genre(genre)
        return render_template('design.html', shows=shows, genre=genre)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


