from django.urls import path
app_name="account"
from .views import UserListView,UserLogout,CreateAdminUser,CreateSpecialUser
urlpatterns=[
    path("")
]