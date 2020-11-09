import jinja2
import sqlite3


# Build dicts from sqlite3 results. See
# https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query.
# The Flask documentation as an alternative version, see
# https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# Helper templating function similar to the one provided by Flask.
templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
templateEnv = jinja2.Environment(loader=templateLoader)
def render_template(filename, **args):
    template = templateEnv.get_template(filename)
    return template.render(**args)


if __name__ == "__main__":
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory

    cursor = conn.cursor()
    cursor.execute('''
        SELECT alpha_2, alpha_3, name
        FROM countries;
    ''')
    records = cursor.fetchall()

    print(render_template('countries.html', countries=records))
