from rest_framework import serializers
 #from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

#from account.api.serializers import UserDetailSerializer
from audiotracks.models import Track
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )


class TrackModelSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = [
            'user',
            'audio_file',
            'image',
            'title',
            'artist',
            'genre',
            'slug'
        ]



class TrackCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = [
            'user',
            'audio_file',
            'image',
            'title',
            'artist',
            'genre',
            'slug'
        ]


class TrackDetailSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = [
            'user',
            'audio_file',
            'image',
            'title',
            'artist',
            'genre',
            'slug'
        ]
class TrackListSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = [
            'user',
            'audio_file',
            'image',
            'title',
            'artist',
            'genre',
            'slug'
        ]


