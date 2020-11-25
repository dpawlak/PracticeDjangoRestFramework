# Django imports
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from django import template

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
from rest_framework.renderers import JSONRenderer
from .filters import PostFilter

# App imports
from .serializers import PostSerializer, TagSerializer
from .models import Post, DoctorProfile, Tag
from .forms import PostForm, DoctorProfileForm



#home view for posts. Posts are displayed in a list
class IndexView(ListView, APIView):
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


#---------------------------------------#
# -------Doctor Profile Views-----------#
#---------------------------------------#

# Doctor List View
class DoctorIndexView(ListView):
    template_name='doctor_index.html'
    context_object_name = 'doctor_list'

    def get_queryset(self):
        return DoctorProfile.objects.all()
    

# Doctor Detail view (view doctor detail)

class DoctorDetailView(DetailView):
 model=DoctorProfile
 template_name = 'doctor-detail.html'


#New Doctor view (Create new post)

def doctorview(request):
 if request.method == 'POST':
  form = DoctorProfileForm(request.POST)
  if form.is_valid():
   form.save()
  return redirect('index')
 form = DoctorProfileForm()
 return render(request,'doctor.html',{'form': form})

#Edit a Doctor

def doctoredit(request, pk, template_name='doctoredit.html'):
    doctor= get_object_or_404(Doctor, pk=pk)
    form = DoctorProfileForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

#Delete post

def doctordelete(request, pk, template_name='doctor_confirm_delete.html'):
    doctor= get_object_or_404(Doctor, pk=pk)    
    if request.method=='POST':
        post.delete()
        return redirect('index')
    return render(request, template_name, {'object':doctor})








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
