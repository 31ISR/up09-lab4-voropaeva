from django import forms 
from . import models 

class CreateCommunities(forms.ModelForm): 
    class Meta: 
        model = models.Communities
        fields = ['name','description','slug','free','banner']