from requests import Response
from rest_framework import viewsets
from django.contrib.auth import get_user_model

User = get_user_model()


class NotificationView(viewsets.GenericViewSet):

    def retrieve_sms(self):
        # business logic  and response will be added in the dictionary
        response = dict()
        return Response(response)

    def retrieve_whatsapp(self):
        #business logic and response will be added in the dictionary
        response = dict()
        return Response(response)

