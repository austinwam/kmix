from rest_framework import serializers
 #from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

from accounts.api.serializers import UserDetailSerializer
from profiles.models import Profile
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )

class ProfileModelSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Profile
        fields = [
            'user',
            'name',
            'bio',
            'picture'
        ]

        
    


          
class ProfileCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'user',
            'name',
            'bio',
            'picture'
        ]

class ProfileDetailSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'user',
            'name',
            'bio',
            'picture'
          ]

 