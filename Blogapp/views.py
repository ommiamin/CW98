from django.shortcuts import render ,redirect
from .models import Post,Author,Category
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


def post_list(request):
    all =Post.objects.all()
    return render(request , 'post_list.html' , {'all':all})

def author_list(request):
    all =Author.objects.all()
    return render(request , 'author_list.html' , {'all':all})

def author(request , Author_id):
    author = Author.objects.get(id= Author_id)
    return render(request , 'author.html',{'author':author})


def category_list(request):
    all =Category.objects.all()
    return render(request , 'category_list.html' , {'all':all})

def category(request , Category_id):
    category = Category.objects.get(id= Category_id)
    return render(request , 'category.html',{'category':category})
    