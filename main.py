from flask import Flask, render_template, url_for, request, redirect
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)

@app.route('/post-field', methods=['GET', 'POST'])
def input_genre():
    genre = request.form['genre']
    shows = queries.get_genre_tops(genre)
    return redirect('index.html')


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


