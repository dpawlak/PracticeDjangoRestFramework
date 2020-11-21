from django.contrib import admin
from .models import Post, DoctorProfile, Tag

admin.site.register(Post)
admin.site.register(DoctorProfile)
admin.site.register(Tag)