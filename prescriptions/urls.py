from django.urls import path
from .views import PrescriptionsView, prescriptionsView, PrescriptionDetailView, prescriptions_chart
from prescriptions import views
 
urlpatterns = [
    path('', views.PrescriptionsView.as_view(), name='prescriptions'),
    path('prescriptions_form/', views.prescriptionsView, name='prescriptions_form'),
    path('prescription_edit/<int:pk>/', views.prescriptionEdit, name='prescription_edit'),
    path('<int:pk>/', views.PrescriptionDetailView.as_view(), name='prescription_detail'),
    path('prescriptions/delete/<int:pk>/', views.delete_prescription, name='delete_prescription'),
    path('prescriptions-chart/', views.prescriptions_chart, name="prescriptions-chart"),
]