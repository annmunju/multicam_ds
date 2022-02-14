# http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson
# ?ServiceKey=jEZ%2F1Uz%2F2yRx7in5f1TnRa1pjjtQvuWhAr9zJ%2FcAbQTwNIU1xw%2FIy2pTkbCZU3KKYSmvTbrNx75aG9eeusevnw%3D%3D
# &pageNo=1
# &numOfRows=10
# &startCreateDt=20200410
# &endCreateDt=20200410

import datetime

now = datetime.datetime.now()
today = str(now.year)+str(now.month)+str(now.day)
print(today)