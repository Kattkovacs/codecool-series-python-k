from flask import Flask, render_template, url_for
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    fourth = queries.get_4th_episodes()
    fifth = queries.get_5th_episodes()
    return render_template('index.html', fourth=fourth, fifth=fifth)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


