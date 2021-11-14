from django.shortcuts import redirect, render
from django.http import HttpResponse

from user.models import Post
from .forms import PostView, UserView
from django.shortcuts import get_object_or_404

# Create your views here.
def Post_view(request):
  if request.method == 'POST':
      ps = PostView(request.POST)
      if ps.is_valid():
          ps.save()
          return redirect('Post')

  else:
      ps = PostView()
      return render(request, 'user/post.html', {'form': ps})


def PostShow(request):
    show = Post.objects.using().all()
    return render(request, 'User/show.html', {'so': show})


def DeletePost(request, id):
    if request.method == 'POST':
        dlt = Post.objects.get(pk=id)
        dlt.delete()
        return redirect('home')


def UpdatePost(request, id):
        obj = get_object_or_404(Post,pk=id)
        updatepost = PostView(request.POST, instance=obj)
        if updatepost.is_valid():
           updatepost.save()
           return redirect('home')

        else:
            
            obj=Post.objects.get(pk=id)
            updatepost= PostView(instance=obj)
            return render(request,'User/update.html',{'form': updatepost}) 
  
     
  
  
def Registration(request):
     if request.method=='POST':
          ro=UserView(request.POST)
          if ro.is_valid():
              ro.save()
     else:
          ro=UserView()
          return render(request,'User/signup.html',{'form':ro})
  
def VIEWNAME(request):
    return HttpResponse('Hello World')

def Htmlview(request):
    return render(request,'User/base.html')

