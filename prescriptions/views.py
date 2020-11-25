# Django imports
from django.shortcuts import render
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

# App imports
from .models import Prescriptions
from .forms import PrescriptionsForm

class PrescriptionsView(ListView, APIView):
    template_name='prescriptions.html'
    context_object_name = 'prescriptions_list'
    
    def get_queryset(self):
        return Prescriptions.objects.all()

#New post view (Create new post)
def prescriptionsView(request):
 if request.method == 'POST':
  form = PrescriptionsForm(request.POST)
  if form.is_valid():
   form.save()
  return redirect('prescriptions')
 form = PrescriptionsForm()
 return render(request,'prescription_form.html',{'form': form})