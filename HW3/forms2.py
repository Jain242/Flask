from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from werkzeug.security import generate_password_hash
from model import User, db

class RegistrationForm(FlaskForm):
    first_name = StringField('Имя', validators=[DataRequired()])
    last_name = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Этот email уже занят, пожалуйста, используйте другой.')

    def save_user(self):
        hashed_password = generate_password_hash(self.password.data)
        user = User(first_name=self.first_name.data, last_name=self.last_name.data, email=self.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
