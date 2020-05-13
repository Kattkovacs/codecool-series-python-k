from flask import Flask, render_template, url_for
from data import queries

app = Flask('codecool_series')


# @app.route('/')
# def index():
#     shows = queries.get_shows_by_deaths()
#     return render_template('index.html', shows=shows)


@app.route('/death/<int:deaths_number>')
def death(deaths_number):
    shows = queries.get_shows_by_deaths(deaths_number)
    return render_template('death.html', shows=shows)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


