from django import forms


class Employeeform(forms.Form):
    Empnum = forms.IntegerField()
    Empname = forms.CharField(max_length=20)
    salary = forms.IntegerField()
    address = forms.CharField(max_length=30)
# Create your models here.


class Deleteform(forms.Form):
    Empnum = forms.IntegerField()


class Updateform(forms.Form):
    Empnum = forms.IntegerField()
    Empname = forms.CharField(max_length=20)
