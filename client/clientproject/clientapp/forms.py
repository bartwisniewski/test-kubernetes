from django import forms


class ClientForm(forms.Form):
    value1 = forms.IntegerField(label="x", initial=2)
    value2 = forms.IntegerField(label="y", initial=2)
