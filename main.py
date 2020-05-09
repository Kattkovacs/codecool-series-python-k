from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        search = request.form['actor_name']

        actors_by_char = queries.get_actors_by_character(actor)
        return render_template('index.html', actors_by_char=actors_by_char)
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)



@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
