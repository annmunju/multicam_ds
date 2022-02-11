# -*- coding:utf-8 -*-

import requests
import json


def getSiDo():
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
    return  sido_dict


def getGuGun(sido_code):
    # __ajaxCall("/store/getGugunList.do", {"sido_cd":sido}, true, "json", "post",
    url = "https://www.starbucks.co.kr/store/getGugunList.do"
    resp = requests.post(url, data={"sido_cd": sido_code})
    gugun_list = resp.json()['list']
    gugun_dict = dict(zip(list(map(lambda x: x['gugun_cd'], gugun_list)),
                          list(map(lambda x: x['gugun_nm'], gugun_list))))
    # print(gugun_dict)
    return gugun_dict


def getStore(sido_code='', gugun_code=''):

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

    return result_dict


def jsonSave(result_dict, sido_code='', gugun_code=''):
    # json 저장
    result_json = json.dumps(result_dict, ensure_ascii=False)
    f_name = getSiDo()[sido_code]+' '+getGuGun(sido_code)[gugun_code]+' 매장정보'
    with open(f'{f_name}.json', 'w', encoding='utf-8') as f:
        f.write(result_json)

    return result_json


if __name__ == '__main__':
    sido_dict = getSiDo()
    print(sido_dict)
    sido = input('도시 코드를 입력해 주세요 : ')
    if sido == '17':
        result_store = getStore(sido_code='17', gugun_code='')
    else:
        gugun_dict = getGuGun(sido)
        print(gugun_dict)
        gugun = input('구군 코드를 입력해 주세요 : ')
        result_store = getStore(gugun_code=gugun)
    print(result_store)
    jsonSave(result_dict=result_store, sido_code=sido, gugun_code=gugun)


