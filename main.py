from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    if request.args.get('selected_type'):
        selected_type = request.args.get('selected_type')
        order = request.args.get('order')
        selected_shows = queries.get_query_by_selection(selected_type, order)
        return render_template('design.html', selected_shows=selected_shows, selected_type=selected_type)
    return render_template('design.html')

def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


