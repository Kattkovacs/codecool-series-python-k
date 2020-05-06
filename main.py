from flask import Flask, render_template, url_for
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_actors_by_character()
    sum_char = 0
    for show in shows:
        sum_char += int(show['played_characters'])
    return render_template('index.html', shows=shows, sum_char=sum_char)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


