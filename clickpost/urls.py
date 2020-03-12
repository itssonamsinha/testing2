from django.urls import path, include
from .router import urlpatterns

urlpatterns = [
    path('clickpost/', include(urlpatterns)),
]