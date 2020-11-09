from flask import Flask, Response, g, jsonify, render_template, request
import json
import sqlite3

# Configure Flask to serve static files, unless a specific route is defined
# below.
# This doesn't serve /index.html when hitting / (this does a 404 instead),
# so the route('/') is explicitely added below.
app = Flask(__name__,
    static_url_path="/",
    static_folder="../_site/")


# Build dicts from sqlite3 results. See
# https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query.
# The Flask documentation as an alternative version, see
# https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# Database connection/query stuff. This is explained in the Flask documentation:
# https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
def get_conn():
    conn = getattr(g, '_database', None)
    if conn is None:
        conn = g._database = sqlite3.connect('app.db')
        conn.row_factory = dict_factory
    return conn

def query(query, args=()):
    cursor = get_conn().execute(query, args)
    records = cursor.fetchall()
    cursor.close()
    return records

@app.teardown_appcontext
def close_connection(exception):
    conn = getattr(g, '_database', None)
    if conn is not None:
        conn.close()


# Show how to return a static file living in the `static_folder` configured
# above.
@app.route('/')
def root():
    return app.send_static_file('index.html')


# Show how to return a string.
@app.route("/hello/1")
def hello_1():
    return """
<html>
<head></head>
<body>
<code><pre>
Hello/1.

This response is hard-coded in `app.py`.


Back to <a href="/">index</a>.
</pre></code>
</body>
</html>
"""


# Show how to return a templated response.
@app.route("/hello/<int:value>")
def hello_template(value):
    return render_template('hello.html', value=value)


# Show how to process a POST request, and send back JSON.
@app.route("/api/echo", methods=["POST"])
def echo():
    message = request.form['message']
    return jsonify({'message': message})


# Show how to query the SQLite database. The query is similar to
# gen-countries-html.py.
@app.route("/api/countries", methods=["GET"])
def countries_json():
    records = query('''
        SELECT alpha_2, alpha_3, name
        FROM countries;
    ''')
    return jsonify(records)


# Same as gen-countries-html.py.
@app.route("/doc/countries.html", methods=["GET"])
def countries():
    records = query('''
        SELECT alpha_2, alpha_2, name
        FROM countries;
    ''')
    return render_template('countries.html', countries=records)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9002)
