from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from api_app import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('api_app.urls')),
    path('prescriptions/', include('prescriptions.urls')),
    path('api/token/', obtain_auth_token, name='obtain-token'),

]
