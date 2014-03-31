# -*- coding: utf-8 -*-
"""
    Syco Logviewer
    ~~~~~~~~~~~~~~

    :author: Daniel Lindh <daniel@cybercow.se>
    :copyright: (c) 2014 System Console project
    :license: see LICENSE for more details.
"""

import os

from sqlalchemy import create_engine
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
    cur = g.con.execute('SELECT title, text FROM entries ORDER BY id DESC')
    entries = cur.fetchall()
    args = {
        'REMOTE_USER': os.environ.get("REMOTE_USER", 'Unknown')
    }

    return render_template('show_entries.html', entries=entries, **args)


@app.route('/log-entries')
def log_entries():
    db = get_db()
    cur = db.execute('SELECT title, text FROM entries ORDER BY id DESC')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


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
    db = get_db()
    cur = db.execute('SELECT title, text FROM entries ORDER BY id DESC')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


@app.route('/alert')
def alert():
    db = get_db()
    cur = db.execute('SELECT title, text FROM entries ORDER BY id DESC')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


if __name__ == '__main__':
    app.run()
