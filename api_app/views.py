# Django imports
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Third party imports 
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets          
from django.views.generic import ListView, DetailView

# App imports
from .serializers import PostSerializer
from .models import Post
from .forms import PostForm

# CRUD app views

#home view for posts. Posts are displayed in a list
class IndexView(ListView):
    template_name='index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.all()
    

#Detail view (view post detail)
class PostDetailView(DetailView):
 model=Post
 template_name = 'post-detail.html'

#New post view (Create new post)
def postview(request):
 if request.method == 'POST':
  form = PostForm(request.POST)
  if form.is_valid():
   form.save()
  return redirect('index')
 form = PostForm()
 return render(request,'post.html',{'form': form})

#Edit a post
def edit(request, pk, template_name='edit.html'):
    post= get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

#Delete post
def delete(request, pk, template_name='confirm_delete.html'):
    post= get_object_or_404(Post, pk=pk)    
    if request.method=='POST':
        post.delete()
        return redirect('index')
    return render(request, template_name, {'object':post})
















# --------------------------------------------------- #

# Practice Views

class TitleList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'post_titles.html'

    def get(self, request):
        queryset = Post.objects.all()
        return Response({'posts': queryset})

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class RetrieveView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class DestroyView(generics.DestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
 
    serializer_class = PostSerializer
    queryset = Post.objects.all()
