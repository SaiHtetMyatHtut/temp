from django import forms


class search_form(forms.Form):
    name = forms.CharField(max_length=100)
