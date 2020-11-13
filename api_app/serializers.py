from rest_framework import serializers
from . models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'patient_name', 
            'description',
            'doctor',
            'department',
            'team',
            'timestamp',
            'id'
        )       

