from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

posts = ['post1','post2','post3']

class Posts:
    counter = 1
    def __init__(self, pid, title, text, creationdate):
        self.pid = Posts.counter
        self.title = ''
        self.text = ''
        self.creationdate = dt.date.today()
        Posts.counter += 1

def index(request):
    return HttpResponse("index")

def all_posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": posts})

def post(request, pid):
    text = posts[pid - 1]
    return render(request, "blog/post.html", {"post_text": text})