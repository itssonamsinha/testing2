import datetime
import json

from django.contrib.sites import requests
from django.db import models
from clickpost.rabbitmq_client import publish_message


class User():
    phone_number = models.CharField(max_length=10, blank=False, null=True, default=None)
    email = models.EmailField(max_length=100, blank=False, null=True, default=None)
    is_phone_number_verified = models.BooleanField(verbose_name='Phone Number Verified', default=False)

    class Meta:
        db_table = "user"


class NotificationAction:
    SMS_NOTIFICATION = 1
    WHATSAPP_Notification = 2
    NOTIFICATION_TYPE_CHOICES = (
        (SMS_NOTIFICATION, "sms_notification"),
        (WHATSAPP_Notification, "whatsapp_notification"),)


class Notification(abc.ABC):
   @abc.abstractmethod
   def send(self):
      pass


class SmsNotification(NotificationAction):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    shipment_id = models.BigIntegerField()
    sent_at = models.DateTimeField(blank=True, null=True, default=None)
    status = models.TextField()

    class Meta:
        db_table = "sms_notification"

    def send(self, user, shipment_id, status):
        sms_noti = SmsNotification.objects.create(user=user,
                                                           shipment_id=shipment_id,
                                                      status=status, sent_at=datetime.datetime.now())
        sms_text = None
        #  create sms text to be send
        message = {
            "data": sms_text,
            "type": "sms"
        }
        # the message to be sent
        publish_message(json.dumps(message))


class WhtsappNotification(NotificationAction):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    shipment_id = models.BigIntegerField()
    sent_at = models.DateTimeField(blank=True, null=True, default=None)
    status = models.TextField()
    template_name = models.CharField(max_length=100, null=False, blank=False)

    def send(self, user, shipment_id, status):
        whatsapp_noti = WhtsappNotification.objects.create(user=user,
                        shipment_id=shipment_id,
                        status=status, sent_at=datetime.datetime.now())
        message = None #the message to be sent
        template_name = None
        # create message over here
        # template_name is the name of the template
        whatsapp_message = {"media": {},
                            "message": "",
                            "template": {
                                "name": template_name,
                                "params": message
                            },
                            "message_type": "HSM"
                            }

        whatsapp_payload = {
            "data": whatsapp_message,
            "type": "whatsapp"
        }
        publish_message(json.dumps(whatsapp_payload))


    class Meta:
        db_table = "whtsapp_notification"


class StatusNotificationTypeRecords():
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    status = models.TextField()
    notification_type = models.PositiveIntegerField(choices=NotificationAction.NOTIFICATION_TYPE_CHOICES)
    is_sent = models.BooleanField(default=False)

    class Meta:
        db_table = "status_notification_type_records"