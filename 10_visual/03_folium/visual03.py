# -*- encoding:utf-8 -*-

import folium
import json

# 1. 서울 성동구 매장정보.json 파일 읽어들이자

with open('서울 성동구 매장정보.json', 'r') as f:
    starbucks1 = json.load(f)

with open('서울 동대문구 매장정보.json', 'r') as f:
    starbucks2 = json.load(f)

starbucks_stores = starbucks1['store_list']+starbucks2['store_list']

# 2. 지도 만들자

location = [37.56392875136698, 127.05444464044996]
starbucks_map = folium.Map(location=location, zoom_start=14)
folium.Marker(location, icon=folium.Icon(color = 'red'), popup=folium.Popup('문주네 집!', max_width=100)).add_to(starbucks_map)

# 3. json 읽은 내용을 가지고 반복해서 starbucks 매장 marker를 만들어 지도 추가하기

for starbucks_store in starbucks_stores:
    location = [starbucks_store['lat'], starbucks_store['lot']]
    folium.Marker(location, popup=folium.Popup(starbucks_store['s_name'], max_width=100)).add_to(starbucks_map)

# 4. 지도 저장하자

starbucks_map.save('visual03.html')