from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import length, equal_to, email,data_required, ValidationError
from market.models import User


class RegisteredForm(FlaskForm):

    def validate_username(selfself,username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('username already exists! Please try a different username')

    def validate_email(self,email_address_to_check):
        email_address=User.query.filter_by(email=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email address already exist!  Please try a different email address')

    username=StringField(label='user name', validators=[length(min=3,max=30),data_required()])
    email_address=StringField(label='email address',validators=[email(),data_required()])
    password1=PasswordField(label='password:',validators=[length(min=6),data_required()])
    password2=PasswordField(label='confirm password:',validators=[equal_to('password1'),data_required()])
    submit=SubmitField(label='Create Account')

class Loginform(FlaskForm):
    username=StringField(label='User Name: ', validators=[data_required()])
    password=StringField(label='password: ',validators=[data_required()])
    submit=SubmitField(label='Sign in')

class PurchaseItemForm(FlaskForm):
    submit=SubmitField(label='Purchase Item')

class SellItemform(FlaskForm):
    submit=SubmitField(label='Sell Item')