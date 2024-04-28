from django.shortcuts import render
from django.http import HttpResponse

posts = ['post1','post2','post3']

def index(request):
    return HttpResponse("index")

def all_posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": posts})

def post(request, pid):
    text = posts[pid - 1]
    return render(request, "post.html", {"post_text": text})