from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    post = Post.objects.all()
    context= {'posts':post }
    template_name = 'cmsapp/home.html'
    return render(request, template_name, context)

def detailed(request, slug):
    post_details = Post.objects.get(slug=slug)
    recent_post = Post.objects.exclude(post_id__exact=post_details.post_id)[:5]
    
    context= { 'post_details':post_details,'recent_post':recent_post }
    template_name = 'cmsapp/detailed.html'
    return render(request, template_name, context)