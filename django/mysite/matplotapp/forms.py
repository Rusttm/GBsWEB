from django import forms

class UploadFunction(forms.Form):
    function_string = forms.CharField(max_length=50)
