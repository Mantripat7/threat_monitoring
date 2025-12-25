from django.db import models

class Event(models.Model):
    SEVERITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("Critical", "Critical"),
    ]

    source_name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=50)
    severity = models.CharField(max_length=10,choices=SEVERITY_CHOICES,db_index=True)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]
        indexes = [
            models.Index(fields=["severity"]),
            models.Index(fields=["timestamp"]),
        ]

    def __str__(self):
        return f"{self.source_name} - {self.severity}"


class Alert(models.Model):
    STATUS_CHOICES = [
        ("Open", "Open"),
        ("Acknowledged", "Acknowledged"),
        ("Resolved", "Resolved"),
    ]

    event = models.OneToOneField(Event,on_delete=models.CASCADE,related_name="alert")
    status = models.CharField(max_length=15,choices=STATUS_CHOICES,default="Open",db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["status"]), models.Index(fields=["created_at"])]

    def __str__(self):
        return f"Alert for Event {self.event.source_name} - {self.status}"
