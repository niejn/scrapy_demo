import zeep
import pandas as pd
import asyncio
import asyncio
import time

import zeep

from zeep.asyncio import AsyncTransport

wsdl = 'http://10.21.2.75:8080/service/LBEBusiness?wsdl'
transport = zeep.Transport(cache=None)
client = zeep.Client(wsdl=wsdl, transport=transport)
login_ans = client.service.login("ZXQH_GPXZ", "GPXZ123321", "myapp", "plain", ""),
sessionId = login_ans[0].sessionId
result = []


def handle_future(future):
    result.extend(future.result())
    print('*' * 200)
    print(result)
    print('*' * 200)


# wsdl = 'http://10.21.2.75:8080/service/LBEBusiness?wsdl'
# client = zeep.Client(wsdl=wsdl)
# sessionId = client.service.login("ZXQH_GPXZ", "GPXZ123321", "myapp", "plain", "")
# print(client.service.login("ZXQH_GPXZ", "GPXZ123321", "myapp", "plain", ""))
# factory = client.type_factory('ns0')


# async def get_payment():
#     delay_minutes = random.randrange(10)
#     await asyncio.sleep(delay_minutes)

async def get_data_by_userid(userid):
    string_type = client.get_type('xsd:string')
    lbParameter_type = client.get_type('ns0:lbParameter')
    queryOption_type = client.get_type('ns0:queryOption')
    par_dict = {"KSRQ": "2018-11-01", "JSRQ": "2018-11-10", "KHH": userid}
    params = []
    for key in par_dict:
        val = par_dict[key]
        temp_lbParameter = lbParameter_type(name=key, value=val)
        params.append(temp_lbParameter)
    valueOption_type = client.get_type('ns0:valueOption')
    valueOption = valueOption_type('VALUE')
    batchNo = 1
    batchSize = 3000
    mqueryOption = queryOption_type(batchNo=batchNo, batchSize=batchSize, queryCount=True, valueOption=valueOption)
    await client.service.query(sessionId.sessionId, "cxSqlKHCJMX", params, "", mqueryOption)


df = pd.read_excel('../input/客户名单（服务器托管）.xlsx')
df = df.apply(pd.to_numeric, errors='ignore')
df['资金账号']
ans_list = []
loop = asyncio.get_event_loop()

transport = AsyncTransport(loop, cache=None)

# for i in df['资金账号']:
#     t = str(i)
#     print(t)
#     ans = get_data_by_userid(t)
#     ans_list.append(ans)
userids = df['资金账号'].tolist()
# tasks = list(map(get_data_by_userid, userids))
string_type = client.get_type('xsd:string')
lbParameter_type = client.get_type('ns0:lbParameter')
queryOption_type = client.get_type('ns0:queryOption')
par_dict = {"KSRQ": "2018-11-01", "JSRQ": "2018-11-10", "KHH": '100100207'}
params = []
for key in par_dict:
    val = par_dict[key]
    temp_lbParameter = lbParameter_type(name=key, value=val)
    params.append(temp_lbParameter)
valueOption_type = client.get_type('ns0:valueOption')
valueOption = valueOption_type('VALUE')
batchNo = 1
batchSize = 3000
mqueryOption = queryOption_type(batchNo=batchNo, batchSize=batchSize, queryCount=True, valueOption=valueOption)
tasks = [

    client.service.query(sessionId, "cxSqlKHCJMX", params, "", mqueryOption),
]
future = asyncio.gather(*tasks, return_exceptions=True)

future.add_done_callback(handle_future)

st = time.time()
loop.run_until_complete(future)
loop.run_until_complete(transport.session.close())
print("time: %.2f" % (time.time() - st))
print("result: %s", result)
print("")
