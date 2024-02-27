from django.urls import path
from .views import GetUserList

urlpatterns = [
    path('get_user_list/', GetUserList.as_view(), name='item-list'),
]
