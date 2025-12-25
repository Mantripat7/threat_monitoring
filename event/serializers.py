from rest_framework import serializers
from event.models import Event, Alert

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id","source_name","event_type","severity","description","timestamp"]
        read_only_fields = ["id", "timestamp"]
 
class AlertSerializer(serializers.ModelSerializer):
    event_source = serializers.CharField(source="event.source_name", read_only=True)
    event_type = serializers.CharField(source="event.event_type", read_only=True)
    severity = serializers.CharField(source="event.severity", read_only=True)

    class Meta:
        model = Alert
        fields = ["id","event_source","event_type","severity","status","created_at"]
        read_only_fields = ["id","event_source","event_type","severity","created_at"]


