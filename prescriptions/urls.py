from django.urls import path
from .views import PrescriptionsView, prescriptionsView
from prescriptions import views

urlpatterns = [
    path('', PrescriptionsView.as_view(), name='prescriptions'),
    path('prescriptions_form/', views.prescriptionsView, name='prescriptions_form'),

]