from django.http import HttpResponse
from requests import Response
from rest_framework import viewsets
from rest_framework import status
from clickpost.models import User, StatusNotificationTypeRecords


class NotificationView(viewsets.GenericViewSet):

    def retrieve_sms(self, request):
        # business logic  and response will be added in the dictionary
        response = dict()
        return HttpResponse("transaction ID and details")

    def retrieve_whatsapp(self):
        #business logic and response will be added in the dictionary
        response = dict()
        print('transaction ID and details')
        return HttpResponse("transaction ID and details")

    def send_notification(self, request):
        user_id = request.GET.get('user_id', None)
        status = request.GET.get('status', None)
        shipment_id = request.GET.get('shipment_id', None)
        notification_type = request.GET.get('notification_type', None)
        if not user_id or not status or not shipment_id or not notification_type:
            return HttpResponse("user id or status or shipment id  or notification_type is missing")

        user = User.objects.filter(id=user_id).first()
        if not user or user.is_verified == False:
            return HttpResponse("user id is not authorized")

        StatusNotificationTypeRecords.objects.create(user_id=user_id, status=status, notification_type=notification_type)
        return HttpResponse("success")




