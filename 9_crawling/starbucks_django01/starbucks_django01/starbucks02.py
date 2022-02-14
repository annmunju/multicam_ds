# -*- coding:utf-8 -*-

import requests
import json


def getSiDo():
    global sido_code, sido_nm

    url = "https://www.starbucks.co.kr/store/getSidoList.do"
    resp = requests.post(url)
    sido_ls = resp.json()['list']

    sido_code = list()
    sido_nm = list()

    for i in range(len(sido_ls)):
        sido_code.append(sido_ls[i]['sido_cd'])
        sido_nm.append(sido_ls[i]['sido_nm'])

    # sido_code = list(map(lambda x: x['sido_cd'], sido_ls)
    # sido_nm = list(map(lambda x: x['sido_nm'], sido_ls)
    sido_dict = dict(zip(sido_code, sido_nm))

    return sido_dict

def getGugun(sido_code):
    url = "https://www.starbucks.co.kr/store/getGugunList.do"
    resp = requests.post(url, data={'sido_cd':sido_code})
    gugun_ls = resp.json()['list']

    gugun_code = list(map(lambda x: x['gugun_cd'], gugun_ls))
    gugun_nm = list(map(lambda x: x['gugun_nm'], gugun_ls))
    gugun_dict = dict(zip(gugun_code, gugun_nm))

    return gugun_dict

result_list = list()
def getStore(sido_code='', gugun_code=''):
    global result_list
    # var storeInterfaceUrl = "/store/getStore.do?r=" + rndCod;
    # __ajaxCall(storeInterfaceUrl,$search, true, "json", "post",
    url = 'https://www.starbucks.co.kr/store/getStore.do'
    resp = requests.post(url, data={'ins_lat': '37.56682',
                                    'ins_lng': '126.97865',
                                    'p_sido_cd': sido_code,
                                    'p_gugun_cd': gugun_code,
                                    'in_biz_cd':'',
                                    'set_date':''})

    store_list = resp.json()['list']
    # print(store_list[1])
    # s_name, tel, doro_address, lat, lot
    # {'store_list' : [{}, {}, {} ... ]} > json 저장


    for store in store_list:
        store_dict = dict()
        store_dict['s_name'] = store['s_name']
        store_dict['tel'] = store['tel']
        store_dict['doro_address'] = store['doro_address']
        store_dict['lat'] = store['lat']
        store_dict['lot'] = store['lot']
        result_list.append(store_dict)

    return result_list



if __name__ == '__main__':
    # 전국 모든 스타벅스 매장 저장
    # result_list = list()
    for i in getSiDo().keys():
        for j in getGugun(i).keys():
            getStore(i, j)
    print(len(result_list))
    result_dict = dict()
    result_dict['list'] = result_list
    result_json = json.dumps(result_dict, ensure_ascii=False)
    with open(f'starbucks_all.json', 'w', encoding='utf-8') as f:
        f.write(result_json)

# 강사님 답안
#     list_all = list()
#
#     sido_all = getSiDo()
#     for sido in sido_all:
#         if sido == '17':
#             result = getStore(sido_code=sido)
#             list_all.extend(result)
#         else :
#             gugun_all = getGugun(sido)
#             for gugun in gugun_all:
#                 result = getStore(gugun_code=gugun)
#                 list_all.extend(result)
#
#     result_dict = dict()
#     result_dict['list'] = list_all
#
#     result = json.dumps(result_dict, ensure_ascii=False)
#     with open('starbucks_all_teach.json', 'w', encoding='utf-8') as f:
#         f.write(result)
#
