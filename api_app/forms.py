from django import forms
from .models import Post, DoctorProfile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = "__all__"