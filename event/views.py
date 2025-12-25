from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from .permissions import IsAdminUserGroup, IsAnalystOrAdminReadOnly
from .models import Event, Alert
from .serializers import EventSerializer, AlertSerializer

import logging
logger = logging.getLogger(__name__)

 
class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminUserGroup]
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    http_method_names = ["post"]


class AlertViewSet(ModelViewSet):
    serializer_class = AlertSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAnalystOrAdminReadOnly]
    http_method_names = ["get", "patch"]
    
    def get_queryset(self):
        queryset = Alert.objects.select_related("event")
        severity = self.request.query_params.get("severity")
        status = self.request.query_params.get("status")

        if severity:
            queryset = queryset.filter(event__severity__iexact=severity)
        if status:
            queryset = queryset.filter(status__iexact=status)

        return queryset
