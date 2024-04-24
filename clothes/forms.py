from django import forms
from .models import Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.utils.translation import gettext_lazy as _

class Orderform(forms.ModelForm):
      delivery_address=forms.CharField(label='sdsdsds',widget=forms.Textarea(attrs={'rows':1,'style':'resize:none;color:red'}))
      phone_number=forms.CharField(label='شماره تلفن',help_text='')
      color=forms.CharField(label="dfdfffd",show_hidden_initial=False)
      class Meta:
        model=Order
        fields=['name','product_name','size','color','delivery_address','phone_number']
      
        
class signupForm(UserCreationForm):
    email= forms.EmailField(label='1ایمیل',max_length=254)
    username=forms.CharField(label='1نام کاربر',help_text='')
    password1=forms.CharField(label='1رمز عبور',help_text='')
    password2=forms.CharField(label=' 1تایید رمز عبور',help_text='')
    class Meta:
        model=User
        fields=('username','email','password1','password2','id')
class signinForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.fields['username'].label='نام کاربری'
        self.fields['password'].label='رمز عبور'

