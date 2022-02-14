from django.shortcuts import render
from django.http import JsonResponse
import requests


def index(request):
    return render(request, 'index.html')

def getSiDo(request):
    # __ajaxCall("/store/getSidoList.do", {}, true, "json", "post",
    url = "https://www.starbucks.co.kr/store/getSidoList.do"
    resp = requests.post(url)
    # print(resp)
    # print(resp.json())
    sido_list = resp.json()['list']
    # print(sido_list[3])

    sido_code = list(map(lambda x: x['sido_cd'], sido_list))
    sido_nm = list(map(lambda x: x['sido_nm'], sido_list))
    # print(sido_code)
    # print(sido_nm)
    sido_dict = dict(zip(sido_code, sido_nm))
    # print(sido_dict)
    return JsonResponse(sido_dict)


def getGuGun(request):
    sido_code = request.GET['sido_code']
    # __ajaxCall("/store/getGugunList.do", {"sido_cd":sido}, true, "json", "post",
    url = "https://www.starbucks.co.kr/store/getGugunList.do"
    resp = requests.post(url, data={"sido_cd": sido_code})
    gugun_list = resp.json()['list']
    gugun_dict = dict(zip(list(map(lambda x: x['gugun_cd'], gugun_list)), list(map(lambda x: x['gugun_nm'], gugun_list))))
    # print(gugun_dict)
    return JsonResponse(gugun_dict)



def getStore(request):

    code = request.GET['code']
    sido_code = code if code == '17' else ''
    gugun_code = '' if code == '17' else code

    url = 'https://www.starbucks.co.kr/store/getStore.do'
    resp = requests.post(url, data={'ins_lat': '37.502976',
                                    'ins_lng': '127.0513664',
                                    'p_sido_cd': sido_code,
                                    'p_gugun_cd': gugun_code,
                                    'in_biz_cd': '',
                                    'set_date': ''})
    store_list = resp.json()['list']
    # s_name, tel, doro_address, lat, lot

    result_list = list()
    for store in store_list:
        store_dict = dict()
        store_dict['s_name'] = store['s_name']
        store_dict['tel'] = store['tel']
        store_dict['doro_address'] = store['doro_address']
        store_dict['lat'] = store['lat']
        store_dict['lot'] = store['lot']
        result_list.append(store_dict)

    # print(result_list)

    # {'store_list': [{'s_name':..., 'tel': ... ,},{},{}]}
    result_dict = dict()
    result_dict['store_list'] = result_list
    print(result_dict)

    return JsonResponse(result_dict)