from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
def index(request):
    return render(request, 'gallery/index.html')