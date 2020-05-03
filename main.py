from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/', methods=["POST", "GET"])
def index():
    shows = queries.get_shows()
    print(shows)
    return render_template('index.html', shows=shows)


@app.route('/design', methods=["POST", "GET"])
def design():
    year = request.args.get('year')
    shows = queries.get_shows_by_given_year(year)
    for show in shows:
        age_of_show = 2020-show['s_year']
        actors_age = show['age']
        age_of_actor_at_release = show['age'] - age_of_show
        show['age_at_release'] = age_of_actor_at_release
        show['age_of_show'] = age_of_show
        if actors_age > age_of_show:
            show['older_then_show'] = 'older'
        else:
            show['older_then_show'] = 'not older'
    print(shows)

    return render_template('design.html', shows=shows, year=year)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
