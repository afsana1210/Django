from django import forms


class ContactForm(forms.Form):
    full_name=forms.CharField()
    email=forms.EmailField()
    content=forms.CharField(widget=forms.Textarea)

# class BlogPostForm(forms.Form):
#     title=forms.CharField()
#     slug=forms.SlugField()
#     content=forms.CharField(widget=forms.Textarea)



