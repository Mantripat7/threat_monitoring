from django.db.models.signals import post_save
from django.dispatch import receiver

from event.models import Event, Alert

import logging
logger = logging.getLogger(__name__)
 


@receiver(post_save, sender=Event)
def create_alert_for_critical_events(sender, instance, created, **kwargs):
    """
    Automatically create an alert when a High or Critical event is created.
    """
    if not created:
        logger.info(f"Event {instance} not created, skipping alert creation")
        return

    if instance.severity in ["High", "Critical"]:
        logger.info(f"Creating alert for {instance.severity} event: {instance}")
        Alert.objects.create(event=instance)
