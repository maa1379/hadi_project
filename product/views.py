from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from .models import Internal, Exportal
from django.views.generic import ListView
from .forms import UploadForm


# Create your views here.
class InternalListView(ListView):
    model = Internal
    template_name = "product/internal_list.html"


class LineListView(ListView):
    queryset = Internal.objects.filter(line=True)
    template_name = "product/line_list.html"


class ExportalListView(ListView):
    model = Exportal
    template_name = "product/exportal_list.html"





def store_internal(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                model=Internal,
                mapdict=['mine',
                         'kode_sine_kar',
                         'shomareh_serail_qoleh_dr_madan',
                         'stone_name',
                         'kode_darage_bandi',
                         'tonazh_taghribi ',
                         'uniqu_id',
                         'uploder',
                         'image1',
                         'image2',
                         'image3',
                         'image4', ])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        return render(request, 'product/add_internal.html', {})





def store_exportal(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                model=Internal,
                mapdict=[
                    'mine',
                    'kode_sine_ka',
                    'kode_peleh',
                    'stone_name',
                    'created',
                    'shomareh_serail_qoleh_dr_madan',
                    'kode_darz',
                    'kode_ghavareh',
                    'kode_rang',
                    'length',
                    'width ',
                    'height',
                    'vazne_taghribi',
                    'vazne_baskol',
                    'uniqu_id',
                    'uploder',
                    'image1',
                    'image2',
                    'image3',
                    'image4',
                ])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        return render(request, 'product/add_exportal.html', {})
