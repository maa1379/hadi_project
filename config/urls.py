from django.urls import path
from .views import Panel,send_mail,BuyeListView,PatinetUserList,VipUserListView

app_name = "config"
urlpatterns = [
    path("", Panel.as_view(), name="config"),
    path("send_email/", send_mail, name="send_email"),
    path("buyer_list/", BuyeListView.as_view(), name="buyer"),
    path("pastient/", PatinetUserList.as_view(), name="patient"),
    path("vip_user/", VipUserListView.as_view(), name="vip"),
]
