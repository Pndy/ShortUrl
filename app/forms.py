from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, URL
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=24)], render_kw={"placeholder": "Username"})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=64)], render_kw={"placeholder": "Password"})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=24)], render_kw={"placeholder": "Username"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email account"})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=64)], render_kw={"placeholder": "Password"})
    password2 = PasswordField(
        'Repeat password', validators=[DataRequired(), EqualTo('password')],
        render_kw={"placeholder": "Repeat password"})
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please us a different email address.')


class UrlForm(FlaskForm):
    url = StringField('Url', validators=[DataRequired(), URL()], render_kw={"placeholder": "https://google.com"})
    submit = SubmitField('Submit')
