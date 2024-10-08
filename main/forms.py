from django import forms
class UserForm(forms.Form):
 name = forms.CharField(label="Модель степлера")
 age = forms.IntegerField(label="Цена")