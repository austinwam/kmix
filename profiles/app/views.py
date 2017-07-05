from django.db.models import Q
from django.utils import timezone

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )

from .pagination import StandardResultsPagination
from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

from .permissions import IsOwnerOrReadOnly

from profiles.models import Profile

from .serializers import (
    ProfileCreateUpdateSerializer, 
    ProfileDetailSerializer, 
    ProfileModelSerializer
    )


class ProfileCreateAPIView(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#class ProfileDetailAPIView(RetrieveAPIView):
 #   queryset = Profile.objects.all()
  #  serializer_class = ProfileDetailSerializer
    #lookup_field = 'slug'
   # permission_classes = [AllowAny]
    #lookup_url_kwarg = "abc"


class ProfileUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateUpdateSerializer
    #lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email



class ProfileDeleteAPIView(DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    #lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"

class ProfileSearchAPIView(generics.ListAPIView):
    serializer_class = ProfileModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        qs = Profile.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query)
                    )
        return qs















