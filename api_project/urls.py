from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from api_app.views import PostListCreateView, RetrieveView, DestroyView, RetrieveUpdateDestroyView, TitleList
from api_app import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('api_app.urls')),
    path('retrieve/<int:pk>', RetrieveView.as_view(), name='retrieve'),
    path('destroy/<pk>', DestroyView.as_view(), name='destroy'),
    path('edit/<pk>', RetrieveUpdateDestroyView.as_view(), name='edit'),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('title_list/', TitleList.as_view(), name='title_list'),

]
