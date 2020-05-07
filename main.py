from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        select = request.form['num-select']
        # or request.form.get('num-select')
        titles = queries.get_titles(select)
        return render_template('index.html', titles=titles, select=select)
    return render_template('index.html')


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


