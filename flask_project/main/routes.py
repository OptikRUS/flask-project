from flask import render_template, Blueprint

from flask_project import login_manager
from flask_project.main.config import get_db_connection

main = Blueprint('main', __name__)


@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT name FROM users WHERE id = {user_id};')
    name = cur.fetchall()
    cur.close()
    conn.close()
    return name


# @main.route("/")
# def home():
#     return render_template('home.html')


@main.route("/")
def test():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('test.html', users=users)
