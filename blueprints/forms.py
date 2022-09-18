import wtforms
from wtforms.validators import length, email, EqualTo
from models import EmailCodeModel, UserModel


# add a new thing
class TodoForm(wtforms.Form):
    title = wtforms.StringField(validators=[length(min=1,max=200)])
    content = wtforms.StringField(validators=[length(min=0)])
    category = wtforms.StringField(validators=[length(min=1, max=200)])

# login form
class LoginForm(wtforms.Form):
    # setting username and password format
    username = wtforms.StringField(validators=[length(min=3, max=20)])
    password = wtforms.StringField(validators=[length(min=4, max=20)])


# Registration form
class RegistForm(wtforms.Form):
    email = wtforms.StringField(validators=[email()])
    username = wtforms.StringField(validators=[length(min=1, max=20)])
    catch = wtforms.StringField(validators=[length(min=4, max=4)])
    password = wtforms.StringField(validators=[length(min=6, max=20)])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])

    # check whether the input verified code is as same as the verified code in database
    def validate_catch(self, field):
        input_code = field.data
        email_ = self.email.data
        catch_model = EmailCodeModel.query.filter_by(email=email_).first()
        if not catch_model or catch_model.catch != input_code:
            print(wtforms.ValidationError("Invalid verified code!"))
            raise wtforms.ValidationError("Invalid verified code!")

    # check whether the username has been registrate, if is,then show the error
    # otherwise pass the checking
    def validate_username(self, field):
        username = field.data
        if UserModel.query.filter_by(username=username).first():
            name_model = UserModel.query.filter_by(username=username).first()
            if username == name_model.username:
                print(wtforms.ValidationError("This account has been registered!"))
                raise wtforms.ValidationError("This account has been registered!")
