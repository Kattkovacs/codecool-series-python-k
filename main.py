from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        year = request.post('year')
        shows = queries.get_shows_by_given_year(year)
        print(shows)
        return render_template('index.html', shows=shows, year=year)
    shows = queries.get_shows()
    print(shows)
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


