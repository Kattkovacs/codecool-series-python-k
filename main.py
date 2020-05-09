from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    year = request.args.get('year')
    shows = queries.get_actors_by_year(year)
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


