from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    return render_template('search.html')


@app.route('/shows-by-name', methods=["POST", "GET"])
def design():
    if request.method == "POST":
        original_search = request.form['search']
        search = '%' + original_search + '%'
        shows = queries.get_show_by_title(search)
    return render_template('index.html', shows=shows, search=original_search)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


