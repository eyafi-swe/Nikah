from django import forms
from nikah.models import post

class postForm(forms.ModelForm):
    details = forms.CharField(max_length=1500,widget=forms.Textarea(attrs={'class':'w3-input w3-boder w3-light-grey w3-padding w3-round','placeholder':'বিস্তারিত...','style':'resize: none;','rows':'4'}
    ),label="")
    class Meta:
        model = post
        fields = ['details',]