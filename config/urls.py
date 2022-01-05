from django.urls import path
from .views import Panel,Send_Email,EmailListView

app_name = "config"
urlpatterns = [
    path("", Panel.as_view(), name="config"),
    path("send_email/", Send_Email.as_view(), name="send_email"),
    path("email_list/", EmailListView.as_view(), name="email_list"),
]
