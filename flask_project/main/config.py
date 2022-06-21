import psycopg2


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'


def get_db_connection():
    connect = psycopg2.connect(
        database="flask_db",
        user='optikrus',
        password='password123456',
        host="127.0.0.1",
        port="5432"
    )
    return connect
