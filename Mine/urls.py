from .views import MadanListView
from django.urls import path
from .views import MadanListView,MadanDetail
app_name="madan"

urlpatterns=[
    path("mada/",MadanListView.as_view(),name="madan_list"),
    path("mada/<int:id>/",MadanDetail.as_view(),name="madan_detail"),
]