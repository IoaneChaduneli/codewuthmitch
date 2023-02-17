from django.shortcuts import render, redirect
from blog.forms import CreateBlogPostForm
from blog.models import BlogPost
from account.models import Account

# Create your views here.

def create_blog_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('account:must_authenticate')

    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email = user.email).first()
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()

    context['form'] =form
    return render(request, 'blog/create_blog.html', context)
