from xml.etree import ElementTree
import requests
import re


service_key = 'jEZ%2F1Uz%2F2yRx7in5f1TnRa1pjjtQvuWhAr9zJ%2FcAbQTwNIU1xw%2FIy2pTkbCZU3KKYSmvTbrNx75aG9eeusevnw%3D%3D'
url = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?ServiceKey={service_key}'


resp = requests.get(url)
tree = ElementTree.fromstring(resp.text)

for item in tree[1][0]:
    if item.find('gubun').text == '서울':
        stdDay = re.sub(r'(\D)+','', item.find('stdDay').text)
        # print(stdDay)
        stdDay = stdDay[2:4] + '/' + stdDay[4:6] + '/' + stdDay[6:8]
        print(f"[{stdDay}]")
        print(f"일일합계 : {item.find('incDec').text}")
        print(f"국내발생 : {item.find('localOccCnt').text}")
        print(f"해외발생 : {item.find('overFlowCnt').text}")

# for item in tree[1][0]:
#     stdDay = re.sub(r'(\D)+','', item.find('stdDay').text)
#     # print(stdDay)
#     stdDay = stdDay[2:4] + '/' + stdDay[4:6] + '/' + stdDay[6:8]
#     print(f"[{stdDay}]")
#     print(f"구분 : {item.find('gubun').text}")
#     print(f"일일합계 : {item.find('incDec').text}")
#     print(f"국내발생 : {item.find('localOccCnt').text}")
#     print(f"해외발생 : {item.find('overFlowCnt').text}")
