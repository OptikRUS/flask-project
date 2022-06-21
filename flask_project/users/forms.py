from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user

from flask_project.main.config import get_db_connection


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя:', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль:', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердить пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute(f'SELECT name FROM users WHERE users.name = {username};')
        except:
            cur.close()
            conn.close()
        else:
            raise ValidationError('Это имя занято. Пожалуйста, выберите другое.')

    def validate_email(self, email):
        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute(f'SELECT email FROM users WHERE users.email = {email};')
        except:
            cur.close()
            conn.close()
        else:
            raise ValidationError('Этот email занят. Пожалуйста, выберите другой.')
