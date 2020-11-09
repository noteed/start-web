# This is a helper script used to generate countries.sql. countries.sql is
# versioned and acts as a source-of-truth in this repository (instead of e.g.
# the latest version of pycountry).

import pycountry

print('''
CREATE TABLE countries (
  alpha_2 TEXT NOT NULL,
  alpha_3 TEXT NOT NULL,
  name TEXT NOT NULL,
  numeric TEXT NOT NULL
);

INSERT INTO countries VALUES
''')
last_country = list(pycountry.countries)[-1]
for country in pycountry.countries:
    comma_or_semicolon = \
        ';' if country.alpha_2 == last_country.alpha_2 else ','
    print(
        f'  ("{country.alpha_2}", "{country.alpha_3}", '
        f'"{country.name}", "{country.numeric}"){comma_or_semicolon}')
