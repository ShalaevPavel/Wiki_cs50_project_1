from django import forms

class Creatioal_form(forms.Form):
    entry_name = forms.CharField(label='Form_name', max_length=100)
    content_instance = forms.CharField(label="Form_content", max_length=150)


class Search_form(forms.Form):
    input_data = forms.CharField(label="Search for entry")



