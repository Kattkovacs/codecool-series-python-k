from flask import Flask, render_template, url_for
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/design')
def design():
    shows = queries.get_selected_shows()
    return render_template('design.html', shows=shows)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


