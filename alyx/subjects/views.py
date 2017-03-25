
from .models import Subject

from .serializers import SubjectListSerializer, SubjectDetailSerializer
from rest_framework import generics, permissions
import django_filters
from django_filters.rest_framework import FilterSet


class SubjectFilter(FilterSet):
    alive = django_filters.BooleanFilter(name='alive')

    class Meta:
        model = Subject
        exclude = ['json']


class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectListSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_class = SubjectFilter
    filter_fields = ['__all__', 'alive']


class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'nickname'
