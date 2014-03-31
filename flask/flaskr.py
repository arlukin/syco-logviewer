# -*- coding: utf-8 -*-
"""
    Syco Logviewer
    ~~~~~~~~~~~~~~

    :author: Daniel Lindh <daniel@cybercow.se>
    :copyright: (c) 2014 System Console project
    :license: see LICENSE for more details.
"""

import os
import time

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text
from flask import Flask, request, g, redirect, url_for, render_template, flash


# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE="mysql+mysqlconnector://root:root@127.0.0.1/syslog?charset=utf8",
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))


# Create mysql connection
engine = create_engine(
    app.config['DATABASE'],
    convert_unicode=True, pool_size=50, pool_recycle=3600
)


@app.before_request
def connect_db():
    """Create a connection to the database before each request."""
    if not hasattr(g, 'con'):
        g.con = engine.connect()


@app.teardown_request
def close_db(ex):
    """Close database connection after each request."""
    if hasattr(g, 'con'):
        g.con.close()
        delattr(g, 'con')


@app.route('/')
def logs():
    cur = g.con.execute('SELECT * FROM signed ORDER BY id DESC')
    entries = cur.fetchall()
    args = {
        'REMOTE_USER': os.environ.get("REMOTE_USER", 'Unknown')
    }

    return render_template('signed.html', entries=entries, **args)


@app.route('/log-entries/<date>')
def log_entries(date):
    """Takes a date with format 2013-01-23"""
    day_time = time.strptime(date, '%Y-%m-%d')
    from_date = time.strftime('%Y-%m-%d 00:00:00', day_time)
    to_date = time.strftime('%Y-%m-%d 23:59:59', day_time)

    cur = g.con.execute(
        text(
            'SELECT * FROM SystemEvents '
            'WHERE ReceivedAt BETWEEN :from_date AND :to_date ORDER BY id DESC'
        ),
        from_date=from_date, to_date=to_date
    )

    entries = cur.fetchall()
    args = {
        'REMOTE_USER': os.environ.get("REMOTE_USER", 'Unknown')
    }

    return render_template('log-entries.html', entries=entries, **args)


@app.route('/log-entries', methods=['POST'])
def add_entry():
    db = get_db()
    db.execute('INSERT INTO entries (title, text) VALUES (?, ?)',
               [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('logs'))


@app.route('/exclude')
def exclude():
    cur = g.con.execute('SELECT * FROM exclude ORDER BY id DESC')
    entries = cur.fetchall()
    args = {
        'REMOTE_USER': os.environ.get("REMOTE_USER", 'Unknown')
    }

    return render_template('exclude.html', entries=entries, **args)


@app.route('/alert')
def alert():
    cur = g.con.execute('SELECT * FROM alert ORDER BY id DESC')
    entries = cur.fetchall()
    args = {
        'REMOTE_USER': os.environ.get("REMOTE_USER", 'Unknown')
    }

    return render_template('alert.html', entries=entries, **args)


if __name__ == '__main__':
    app.run()
