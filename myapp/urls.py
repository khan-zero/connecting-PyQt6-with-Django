from django.urls import path
from .views import MyDataView

urlpatterns = [
    path('api/endpoint/', MyDataView.as_view(), name='api-endpoint'),
]
