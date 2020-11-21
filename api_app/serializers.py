from rest_framework import serializers
from . models import Post, DoctorProfile, Tag

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'first_name', 
            'last_name',
            'description',
            'doctor',
            'building',
            'timestamp',
            'tags'
        )       

class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = DoctorProfile
        fields = (
            'doctor_first_name',
            'doctor_last_name',
            'doctor_summary'
        )

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag 
        fields = (
            'name',
        )