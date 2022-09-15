import wtforms
from wtforms.validators import length,email,EqualTo
from models import EmailCodeModel,UserModel

#login form
class LoginForm(wtforms.Form):
    #没写验证核对部分
    username=wtforms.StringField(validators=[length(min=3,max=20)])
    password=wtforms.StringField(validators=[length(min=4,max=20)])
    # def validate_password(self,field):
    #     input_password=field.data
    #     username=self.username.data
    #     possible_user = UserModel.query.filter_by(username=username).first()
    #     if not possible_user or possible_user.password != input_password:
    #         print(wtforms.ValidationError("Invalid password!"))
    #         raise wtforms.ValidationError("Invalid password!")
# 注册表单
class RegistForm(wtforms.Form):
    email = wtforms.StringField(validators=[email()])
    username = wtforms.StringField(validators=[length(min=1, max=20)])
    catch = wtforms.StringField(validators=[length(min=4, max=4)])
    password = wtforms.StringField(validators=[length(min=6, max=20)])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])

    # # 进一步验证某一个字段——提交的catch验证码是否和数据库中查询到邮箱一致的用户验证码相同
    def validate_catch(self, field):
        input_code = field.data
        email_ = self.email.data
        catch_model = EmailCodeModel.query.filter_by(email=email_).first()
        if not catch_model or catch_model.catch != input_code:
            print(wtforms.ValidationError("Invalid verified code!"))
            raise wtforms.ValidationError("Invalid verified code!")
    #
    def validate_username(self, field):
        username = field.data
        if UserModel.query.filter_by(username=username).first():
            name_model = UserModel.query.filter_by(username=username).first()
            if username == name_model.username:
                print(wtforms.ValidationError("This account has been registered!"))
                raise wtforms.ValidationError("This account has been registered!")
