from django.urls import path
from .views import GetDriverList

urlpatterns = [
    path('get_user_list/', GetDriverList.as_view(), name='item-list'),
]
