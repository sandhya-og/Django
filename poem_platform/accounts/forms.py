from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Poem, Profile, Category, Tag
from ckeditor.widgets import CKEditorWidget

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class PoemForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    
    class Meta:
        model = Poem
        fields = ['title', 'content', 'categories', 'tags']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']
