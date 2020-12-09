from django.urls import path
from . import views

urlpatterns = [
    # Appoinments
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('post/', views.postview, name='post'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    
    # Doctor Profile 
    path('doc', views.DoctorIndexView.as_view(), name='doctor_index'),
    path('doctor/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctor/edit/<int:pk>/', views.doctoredit, name='doctor_edit'),
    path('doctor/', views.doctorview, name='doctor'),
    path('doctor/delete/<int:pk>/', views.doctordelete, name='doctor_delete'),
    
    # Pie Chart
    path('pie-chart/', views.pie_chart, name='pie-chart')
]