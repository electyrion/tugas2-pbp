from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.


def show_watchlist(request):
    data_list_movie = MyWatchList.objects.all()
    context = {
        'list_movie': data_list_movie,
        'nama': 'Muhammad Vicky Maulana',
        'npm': '2106750906',
    }
    return render(request, "mywatchlist.html", context)


def show_xml(request):
    # menyimpan hasil query dari seluruh data yang ada pada BarangwishList
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
