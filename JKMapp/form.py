from django import forms
from JKMapp.models import Employee ,Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PersonalDetails



class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class StuForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

#from django import forms  
class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 100)  



class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ['first_name', 'last_name', 'email', 'phone_number']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)