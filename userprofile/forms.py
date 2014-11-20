from django import forms
from models import UserProfile

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile 
        fields = ('foretag', 'orgnr', 'foretagsbeskrivning', 'address', 'stad', 'postnr')