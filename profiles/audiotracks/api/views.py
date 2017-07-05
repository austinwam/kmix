from django.db.models import Q
from django.utils import timezone
from rest_framework import generics
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from .pagination import StandardResultsPagination	
	
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    #UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )



from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

from .permissions import IsOwnerOrReadOnly

from audiotracks.models import Track

from .serializers import (
    TrackCreateUpdateSerializer, 
    TrackDetailSerializer, 
    TrackListSerializer,
	TrackModelSerializer
    )


class TrackCreateAPIView(CreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TrackDetailAPIView(RetrieveAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackDetailSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    #lookup_url_kwarg = "abc"


class TrackUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackCreateUpdateSerializer
    #lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email



class TrackDeleteAPIView(DestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"


class SearchAPIView(generics.ListAPIView):
    serializer_class = TrackModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        qs = Track.objects.all().order_by("-timestamp")
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query)
                    )
        return qs














