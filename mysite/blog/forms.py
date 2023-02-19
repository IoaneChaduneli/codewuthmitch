from django import forms
from blog.models import BlogPost

class CreateBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'text',   
            'image' 
        ]

class UpdateBlogPostFom(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'text',
            'image'
        ]

    def save(self, commit: bool = True):
        blog_post = self.instance
        blog_post.title = self.cleaned_data['title']
        blog_post.text = self.cleaned_data['text']

        if self.cleaned_data['image']:
            blog_post.image = self.cleaned_data['image']
        
        if commit:
            blog_post.save()
        return blog_post