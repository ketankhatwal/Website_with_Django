from django.shortcuts import render
from posts.models import Post

def home(request):
	context={
		'posts':Post.objects.all()
	}
	return render(request,'social/home.html',context,{'title':'Home'})


def about(request):
	return render(request,'social/about.html',{'title':'About'})

def gallery(request):
	return render(request,'social/gallery.html',{'title':'Gallery'})