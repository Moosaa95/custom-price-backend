from django import forms 


class OptionForm(forms.Form):
    product_id = forms.CharField(max_length=10)
    selected_options = forms.CharField(max_length=200)
    quantity = forms.CharField(max_length=20)