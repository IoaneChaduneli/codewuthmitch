from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from blog.forms import CreateBlogPostForm, UpdateBlogPostFom
from blog.models import BlogPost
from account.models import Account
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse



# Create your views here.
@login_required(login_url='/authenticate/')
def create_blog_view(request):

    context = {}
    user = request.user
    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
       obj = form.save(commit=False)
       author = Account.objects.filter(email=user.email).first()
       obj.author = author
       obj.save()

    context['form'] = form
    return render(request, 'blog/create_blog.html', context)


def detail_blog_view(request, slug):
   context = {}

   Blog_post = get_object_or_404(BlogPost, slug=slug)
   context['blog_post'] = Blog_post
   return render(request, 'blog/post_detail.html', context)

def update_blog_view(request, slug):
   context ={}
   user = request.user
   blog_post = get_object_or_404(BlogPost, slug=slug)
   if blog_post.author != user:
      return HttpResponse('You are not the author of that post.')
   if request.POST:
      form = UpdateBlogPostFom(request.POST or None, request.FILES or None, instance=blog_post)
      if form.is_valid():
         obj = form.save(commit=False)
         obj.save()
         context['success_message'] = "Successfully Updated"
         blog_post = obj
         
   form = UpdateBlogPostFom(

         initial = {
            'title': blog_post.title,
            'text' : blog_post.text,
            'image': blog_post.image,
         }

   )
   context['form'] = form
   return render(request, 'blog/edit_blog.html', context)


def delete_blog_view(request, slug):
   context ={}
   blog_post = get_object_or_404(BlogPost, slug=slug)
   if blog_post.author != request.user:
      return HttpResponse('You are not the author of that post.')
   
   context['blog_post'] = blog_post

   if request.POST:
      blog_post.delete()
      return redirect('personal:home')
   return render(request, 'blog/blog_delete.html', context)

def get_blog_queryset(query=None):
   queryset = []
   quaries = query.split(' ')
   for q in quaries:
      posts = BlogPost.objects.filter(
               Q(title__icontains=q) |
               Q(text__icontains=q) 
            ).distinct()

      for post in posts:
         queryset.append(post)
   return list(set(queryset))