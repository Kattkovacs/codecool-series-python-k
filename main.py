from flask import Flask, render_template, url_for
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    episodes_sum = queries.get_episodes_sum()
    for episode in episodes_sum:
        if episode['episodes'] > 100:
            episode['is_long'] = True
        else:
            episode['is_long'] = False
    shows = queries.get_shows()
    return render_template('index.html', shows=shows, episodes_sum=episodes_sum)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


