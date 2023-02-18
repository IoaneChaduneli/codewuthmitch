from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from blog.forms import CreateBlogPostForm
from blog.models import BlogPost
from account.models import Account
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required(login_url='/authenticate/')
def create_blog_view(request):

    context = {}
    user = request.user
    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    print(form)
    if form.is_valid():
       obj = form.save(commit=False)
       author = Account.objects.filter(email=user.email).first()
       obj.author = author
       obj.save()

    context['form'] = form
    return render(request, 'blog/create_blog.html', context)


