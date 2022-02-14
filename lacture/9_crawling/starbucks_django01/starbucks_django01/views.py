from django.shortcuts import render
from django.http import JsonResponse
from . import starbucks02

def index(request):
    return render(request, 'index.html')


def starbucks(request):
    for i in starbucks02.getSiDo().keys():
        for j in starbucks02.getGugun(i).keys():
            starbucks02.getStore(i, j)
    result_dict = dict()
    result_dict['list'] = starbucks02.result_list

    return JsonResponse(result_dict)