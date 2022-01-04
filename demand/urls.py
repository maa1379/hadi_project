from django.urls import path
from .views import VisitListView,HoldListView,ForbidenWordListView,ForbidenCreate


app_name="demand"
urlpatterns=[
    path("visit_list/",VisitListView.as_view(),name="visit"),
    path("hold_list/",HoldListView.as_view(),name="hold"),
    path("forbiden/",ForbidenWordListView.as_view(),name="forbiden_list"),
    path("forbiden/create/",ForbidenCreate.as_view(),name="forbiden_create"),
]