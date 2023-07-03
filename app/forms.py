from flask_wrf import FlaskForm
from wtforms import StringFiled, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleandField('Remember Me')
  sibmit = SubmitField('Sing In')