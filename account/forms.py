from django import forms
from django.contrib.auth.models import User

class userRegisterForm(forms.ModelForm):
	password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
	class Meta:
		model = User
		#fields ='__all__'
		fields = {'first_name','last_name','email','username','password'}
		widgets = {
			'first_name':forms.TextInput(attrs={'class':'form-control'}),
			'last_name':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
			'username':forms.TextInput(attrs={'class':'form-control','auto-focus':'true'}),
		}