from django import forms

class SearchForm(forms.Form):
    question = forms.CharField(label='Question', max_length=256)
