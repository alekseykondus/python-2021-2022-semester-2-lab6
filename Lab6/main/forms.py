from django import forms


class UserForm(forms.Form):
    categoryProduct_id = forms.IntegerField()