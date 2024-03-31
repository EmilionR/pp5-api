from rest_framework import generics, permissions
from .models import Report
from .serializers import ReportSerializer, ReportDetailSerializer
from drf_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class ReportList(generics.ListCreateAPIView):
    """
    List all reports
    If logged in, create a report
    """
    queryset = Report.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a report
    if you're the owner, update or delete the report
    """
    queryset = Report.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReportDetailSerializer
