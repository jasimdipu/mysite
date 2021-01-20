from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.

# def index(request):
#     my_dict = {"insert_me": "I am from views py file"}
#     return render(request, 'index.html', context=my_dict)

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetails(generic.DetailView):
    model = Post
    template_name = 'post_details.html'
