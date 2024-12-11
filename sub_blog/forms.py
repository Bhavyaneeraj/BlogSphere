from django import forms

from .models import posts,Tags,Author,CommentsModel
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):
    tags = forms.CharField(max_length=200, required=False, help_text="Enter comma-separated tags.")

    class Meta:
        model = posts
        exclude = ['date', 'slug', 'tag','Author_details',  ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()  
            tags_input = self.cleaned_data['tags']
            if tags_input:
                tag_names = [t.strip() for t in tags_input.split(',')]
                for name in tag_names:
                    tag, created = Tags.objects.get_or_create(simple_tag=name)
                    instance.tag.add(tag)

        return instance
    
class AuthorDetailForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']  
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=CommentsModel
        fields = ['name','comment',]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Your Comment','rows': '1', 'cols': '35'}),
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )







