from django.urls import path
from .views import GetDriverList

urlpatterns = [
    path('getir_arac/get_user_list/', GetDriverList.as_view(), name='item-list'),
]
