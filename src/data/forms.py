from flask_wtf import FlaskForm
import wtforms



class SignUp(FlaskForm):
    first_name = wtforms.StringField("імя")
    last_name = wtforms.StringField("прізвище")
    email = wtforms.EmailField("бистро емаіл піші", validators=[wtforms.validators.data_required(), wtforms.validators.Email()])
    password = wtforms.PasswordField("пароль", validators=[wtforms.validators.length(6)])
    submit = wtforms.SubmitField("Заееструватися")

class LoginForm(FlaskForm):
    email = wtforms.EmailField("бистро емаіл піші", validators=[wtforms.validators.data_required(), wtforms.validators.Email()])
    password = wtforms.PasswordField("пароль", validators=[wtforms.validators.length(6)])
    submit = wtforms.SubmitField("Заееструватися")