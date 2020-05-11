from flask import Flask, render_template, url_for
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    actors = queries.get_actors_with_genres()
    return render_template('index.html', actors=actors)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


