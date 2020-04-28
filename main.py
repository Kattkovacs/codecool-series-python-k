from flask import Flask, render_template, url_for, request, redirect
from data import queries

app = Flask('codecool_series')


@app.route('/', methods=['GET', 'POST'])
def index():
    genre = request.args.get('genre')
    shows = queries.get_genre_tops(genre)
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


