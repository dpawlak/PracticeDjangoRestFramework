from django.urls import path
from .views import PrescriptionsView

urlpatterns = [
    path('', PrescriptionsView.as_view(), name='prescriptions'),

]