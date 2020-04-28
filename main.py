from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    return render_template('search.html')


@app.route('/actors-by-date', methods=["POST", "GET"])
def search():
    if request.method == "POST":
        original_search = request.form['search']
        search = '%' + original_search + '%'
        shows = queries.get_actors_by_date(search)
    return render_template('index.html', shows=shows, search=original_search)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


