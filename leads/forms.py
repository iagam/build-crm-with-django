from django import forms


class LeadForm(forms.Form):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    age = forms.IntegerField(min_value=1)
