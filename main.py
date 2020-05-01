from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_search = request.form['search']
        search = f"%{original_search}%"
        shows = queries.get_character_details(search)
        print(shows)
        return render_template('index.html', shows=shows, search=original_search)
    return render_template('index.html')


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


