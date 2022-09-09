from django.shortcuts import render
from katalog.models import CatalogItem
# TODO: Create your views here.


def show_katalog(request):
    data_item_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_item_katalog,
        'nama': 'Vicky'
    }
    return render(request, "katalog.html", context)
