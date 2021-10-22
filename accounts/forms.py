from django import forms
from accounts.models import userProfile
from django.forms import ModelForm


class userProfileForm(forms.ModelForm):
    
    dateOfBirth = forms.DateField(widget=forms.TextInput(
        attrs={'type':'date','class':'w3-input w3-boder  w3-padding w3-round'}
    ),label="জন্ম")
    nationality = forms.CharField(widget=forms.TextInput(
        attrs={'class':'w3-input w3-boder  w3-padding w3-round'}
    ),label="জাতীয়তা")
    bio = forms.CharField(widget=forms.TextInput(
        attrs={'class':'w3-input w3-boder  w3-padding w3-round'}
    ),label="আপনার সম্পর্কে")
    height = forms.CharField(widget=forms.TextInput(
        attrs={'class':'w3-input w3-boder  w3-padding w3-round'}
    ),label="উচ্চতা")
    weight = forms.CharField(widget=forms.TextInput(
        attrs={'class':'w3-input w3-boder  w3-padding w3-round'}
    ),label="ওজন")
    religion = forms.CharField(widget=forms.TextInput(
        attrs={'class':'w3-input w3-boder  w3-padding w3-round'}
    ),label="ধর্ম")
    sex = forms.CharField(widget=forms.TextInput(
        attrs={'class':'w3-input w3-boder  w3-padding w3-round'}
    ),label="লিঙ্গ")
    proffession = forms.CharField(widget=forms.TextInput(
        attrs={'class':'w3-input w3-boder  w3-padding w3-round'}
    ),label="পেশা")
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class':'w3-input w3-boder  w3-padding w3-round'}
    ),label="মোবাইল নম্বর")
    profilePicture = forms.ImageField(required=False, label="প্রোফাইল পিকচার যুক্ত করুন")
    galleryPicOne = forms.ImageField(required=False, label="গ্যালারির জন্য ছবি যুক্ত করুন") 
    galleryPicTwo = forms.ImageField(required=False, label="গ্যালারির জন্য ছবি যুক্ত করুন") 
    galleryPicThree = forms.ImageField(required=False, label="গ্যালারির জন্য ছবি যুক্ত করুন") 
    galleryPicFour = forms.ImageField(required=False, label="গ্যালারির জন্য ছবি যুক্ত করুন") 
    class Meta:
        model = userProfile
        exclude = ('user',)
