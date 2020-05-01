from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/')
def actors():
    shows = queries.get_actors_by_title()
    print(shows)
    return render_template('actors.html', shows=shows)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


