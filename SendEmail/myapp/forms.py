from django import forms

# creating a form
class EmailForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    mobileno = forms.CharField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))