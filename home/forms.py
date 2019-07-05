from django import forms
from .models import *

class StudentSearchForm(forms.Form):
	q = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control',
		'maxlength':'30','placeholder':'search'}))

class AboutForm(forms.Form):
	p = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','placeholder':'about'}))

class StudentEditForm(forms.ModelForm):
	class Meta:
		model =Student
		fields = '__all__'
		widgets = {
			'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Student Name'}),
			'Branch' : forms.Select(attrs={'class':'custom-selelct'})
		}

class StudentCreateForm(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','max_length':'30','placeholder':'Student Name'}))
    #Branch = models.ForeignKey('Department',on_delete=models.SET_NULL,null=True)
    # dept = (('CSE','Computer Science'),('ISE','Information Science'))
    # Branch = forms.CharField(label='',widget=forms.Select(attrs={'class':'form-control'},choices=dept))
    Branch= forms.ModelChoiceField(queryset=Department.objects.all())
