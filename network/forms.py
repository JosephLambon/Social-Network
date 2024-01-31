from django import forms

class NewPostForm(forms.Form):
    title = forms.CharField(max_length=64, required=True)
    body = forms.CharField(widget=forms.Textarea(attrs={'name':'body',
                                 'style': 'height: 3em;'}),max_length=255, required=True)