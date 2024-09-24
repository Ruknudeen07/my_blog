from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from.models import post

# Create your views here.
#static demo deta
# posts = [
#         {'id' : 1,'title' : 'Post 1','content' :'content of post 1'},
#         {'id' : 2,'title' : 'Post 2','content' :'content of post 2'},
#         {'id' : 3,'title' : 'Post 3','content' :'content of post 3'},
#         {'id' : 4,'title' : 'Post 4','content' :'content of post 4'},
 #   ]
def index(request):
    title_name ="Latest Posts"
    #getting data from post model
    
    posts = post.objects.all()
    return render(request,'blog/index.html',{'title_name': title_name,'posts' : posts})

def detail(request, post_id):
    #static deta
    # post = next((item for item in posts if item['id'] == int( post_id)),None)
    
    #gettingmdata frommodel by post id
    
    post = post.objects.get(pk=post_id)
   
    # logger=logging.getLogger('TESTING')
    # logger.warning(f'post variable is {post}')
    return render(request,'blog/detail.html',{'post':post})

def old_url_redirect(request):
    return redirect(reverse("blog:change_url "))

def new_url_view(request):
    return HttpResponse("this is  new url")
