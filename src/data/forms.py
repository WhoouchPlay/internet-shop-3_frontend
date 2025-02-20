from flask_wtf import FlaskForm
import wtforms



class SignUp(FlaskForm):
    name = wtforms.StringField("Ім'я")
    email = wtforms.EmailField("Електронна пошта", validators=[wtforms.validators.data_required(), wtforms.validators.Email()])
    password = wtforms.PasswordField("Пароль", validators=[wtforms.validators.length(6)])
    submit = wtforms.SubmitField("Зареєструватися")

class LoginForm(FlaskForm):
    email = wtforms.EmailField("Електронна пошта", validators=[wtforms.validators.data_required(), wtforms.validators.Email()])
    password = wtforms.PasswordField("Пароль", validators=[wtforms.validators.length(6)])
    submit = wtforms.SubmitField("Увійти в систему")