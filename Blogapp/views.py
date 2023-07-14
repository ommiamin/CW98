from django.shortcuts import render ,redirect
from .models import Post
#from django.http import HttpResponse

# Create your views here.

def home(request):
    all =Post.objects.all()

    return render(request , 'home.html' , {'all':all})

 
def detail(request , Post_id):
    post = Post.objects.get(id= Post_id)
    return render(request , 'detail.html',{'post':post})

def delete(request , post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('home')