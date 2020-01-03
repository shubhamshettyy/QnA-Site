from django.shortcuts import render
from .models import Post, Answer

# Create your views here.

def home(request):

	return render(request,'blog/home.html',context={'posts':Post.objects.all(),
													'answers':Answer.objects.all()
													})
def about(request):

	return render(request,'blog/about.html')

