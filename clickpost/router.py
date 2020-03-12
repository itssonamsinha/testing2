from django.urls import path
from .views import NotificationView

urlpatterns = [
    path('sendSms', NotificationView.as_view({'get': 'retrieve_sms'}), name='send-sms'),
    path('sendWhatsApp', NotificationView.as_view({'get': 'retrieve_whatsapp'}), name='send-sms'),

]