from clickpost.models import StatusNotificationTypeRecords, NotificationAction


class SendMessages:
    def __init__(self):
        pass

    #  we are calling this method for all the entries whose messages have not been sent yet

    def send_notification_message(self, user_id, status):
        records_obj = StatusNotificationTypeRecords.objects.filter(user_id=user_id, status__exact=status, is_sent=False)

        for data in records_obj:
            # check if user is authorized or not (raise error if not)
            if data.notification_type == NotificationAction.SMS_NOTIFICATION:
                obj = NotificationAction.SMS_NOTIFICATION()
            elif data.notification_type == NotificationAction.WHATSAPP_Notification:
                obj = NotificationAction.WHATSAPP_Notification()

            obj.send(data.user, data.shipment_id, data.status)
            data.is_sent = True
            data.save()