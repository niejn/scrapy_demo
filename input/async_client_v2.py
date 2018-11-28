import asyncio
import random
import time

import zeep
from zeep.cache import SqliteCache
from zeep.asyncio import AsyncTransport
import pandas as pd

global sessionId
def run_async():
    print("async example")
    print("=============")

    result = []

    def handle_future(future):
        result.extend(future.result())
        print(future.result())
        # [unicode(x.strip()) if x is not None else '' for x in row]
        record_list = []
        for row in result:
            if len(row.records) == 0:
                continue
            record_list.extend(row.records)
        record_list = [item.values for item in record_list]
        # record_list = [[record for record in row.records] for row in result]
        df = pd.DataFrame.from_records(record_list, columns=None,)
        df.to_csv('../output/crm_test.csv', encoding='gbk')
        asyncio.ensure_future(logout())




    loop = asyncio.get_event_loop()
    wsdl = 'http://10.21.2.75:8080/service/LBEBusiness?wsdl'
    cache = SqliteCache(path='./sqlite.db', timeout=3600)
    transport = AsyncTransport(loop, cache=cache)
    client = zeep.Client(wsdl, transport=transport)
    # login_ans = client.service.login("ZXQH_GPXZ", "GPXZ123321", "myapp", "plain", ""),
    # sessionId = login_ans[0].sessionId
    async def login(future):
        result = await client.service.login("ZXQH_GPXZ", "GPXZ123321", "myapp", "plain", ""),
        global sessionId
        sessionId = result[0].sessionId
        future.set_result(result[0].sessionId)
    async def logout():
        global sessionId
        result = await client.service.logout(sessionId)

        result = await transport.session.close()
        loop.stop()



    def send_quests(future):
        sessionId = future.result()
        df = pd.read_excel('./客户名单（服务器托管）.xlsx')
        df = df.apply(pd.to_numeric, errors='ignore')
        user_ids = df['资金账号'].tolist()
        user_ids = user_ids[0:20]
        tasks = [
            setup_req(sessionId, str(user_id)) for user_id in user_ids
        ]

        future2 = asyncio.gather(*tasks, return_exceptions=True)
        future2.add_done_callback(handle_future)


    async def setup_req(sessionId, user_id,):
        lbParameter_type = client.get_type('ns0:lbParameter')
        queryOption_type = client.get_type('ns0:queryOption')

        par_dict = {"KSRQ": "2018-11-01", "JSRQ": "2018-11-10", "KHH": user_id}
        params = []
        for key in par_dict:
            val = par_dict[key]
            temp_lbParameter = lbParameter_type(name=key, value=val)
            params.append(temp_lbParameter)

        valueOption_type = client.get_type('ns0:valueOption')
        valueOption = valueOption_type('VALUE')
        batchNo = 1
        batchSize = 3000
        mqueryOption = queryOption_type(batchNo=batchNo, batchSize=batchSize,
                                        queryCount=True, valueOption=valueOption)
        #  waits 1 second
        # delay_seconds = random.randrange(5)
        # await asyncio.sleep(delay_seconds)
        # await asyncio.sleep(1)
        result = await client.service.query(sessionId, "cxSqlKHCJMX", params, "", mqueryOption)

        return result

    lbParameter_type = client.get_type('ns0:lbParameter')
    queryOption_type = client.get_type('ns0:queryOption')

    par_dict = {"KSRQ": "2018-11-01", "JSRQ": "2018-11-10", "KHH": "0000050067"}
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



    # st = time.time()
    # loop.run_until_complete(future)
    # loop.run_until_complete(transport.session.close())
    # print("time: %.2f" % (time.time() - st))
    # print("result: %s" % result)
    # print("")
    # print("sessionId:{sessionId}".format(sessionId=sessionId))
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(login(future))
    future.add_done_callback(send_quests)
    try:
        loop.run_forever()
    finally:
        loop.close()
    return result





if __name__ == '__main__':
    print("")
    run_async()

