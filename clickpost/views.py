from requests import Response
from rest_framework import viewsets
from rest_framework import status
from clickpost.config import SendMessages
from clickpost.models import User


class NotificationView(viewsets.GenericViewSet):

    def retrieve_sms(self, request):
        # business logic  and response will be added in the dictionary
        response = dict()
        print('transaction ID and details')
        return Response(status=status.HTTP_200_OK)

    def retrieve_whatsapp(self):
        #business logic and response will be added in the dictionary
        response = dict()
        print('transaction ID and details')
        return Response(status=status.HTTP_200_OK)

    def send_notification(self, request):
        user_id = request.GET.get('user_id', None)
        status = request.GET.get('status', None)
        shipment_id = request.GET.get('shipment_id', None)
        if not user_id or not status or not shipment_id:
            return Response({'success': False, 'message': 'user id or status or shipment id is missing'})

        if user_id:
            user = User.objects.filter(id=user_id).first()
            if not user or user.is_verified == False:
                return Response({'success': False, 'message': 'User not verified'})

        SendMessages.send_notification_message(user_id, status, shipment_id)


