from django.urls import path
from .views import ExportalListView, InternalListView, store_exportal, store_internal
app_name="product"

urlpatterns=[
    path("internal_list/",InternalListView.as_view(),name="internal"),
    path("exportal_list/",ExportalListView.as_view(),name="exportal"),
    path("store_ibternal/",store_internal,name="store_internal"),
    path("store_exportal/",store_exportal,name="store_exportal"),
]