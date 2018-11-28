import asyncio
import time

import zeep

from zeep.asyncio import AsyncTransport


def run_async():
    print("async example")
    print("=============")

    result = []

    def handle_future(future):
        result.extend(future.result())
        print(future.result())

    loop = asyncio.get_event_loop()
    wsdl = 'http://10.21.2.75:8080/service/LBEBusiness?wsdl'
    transport = AsyncTransport(loop, cache=None)
    client = zeep.Client(wsdl, transport=transport)
    # login_ans = client.service.login("ZXQH_GPXZ", "GPXZ123321", "myapp", "plain", ""),
    # sessionId = login_ans[0].sessionId
    lbParameter_type = client.get_type('ns0:lbParameter')
    queryOption_type = client.get_type('ns0:queryOption')
    par_dict = {"KSRQ": "2018-11-13",
                "JSRQ": "2018-11-13",
                "YYB": "1",
                # "TJFL": "0",
                "TJFL": "1",
                }
    params = []
    for key in par_dict:
        val = par_dict[key]
        temp_lbParameter = lbParameter_type(name=key, value=val)
        params.append(temp_lbParameter)
    valueOption_type = client.get_type('ns0:valueOption')
    valueOption = valueOption_type('VALUE')
    batchNo = 1
    batchSize = 30
    mqueryOption = queryOption_type(batchNo=batchNo, batchSize=batchSize, queryCount=True, valueOption=valueOption)
    batchNo += 1
    mqueryOption2 = queryOption_type(batchNo=batchNo, batchSize=batchSize, queryCount=True, valueOption=valueOption)
    mqueryOption0 = queryOption_type(batchNo=batchNo, batchSize=batchSize, queryCount=True, valueOption=valueOption)
    # ans = client.service.query(sessionId.sessionId, "cxSqlKHCJTJ_GPXZ", params, "", mqueryOption)
    # print(ans)

    tasks = [
        # client.service.login("ZXQH_GPXZ", "GPXZ123321", "myapp", "plain", ""),
        client.service.login("ZXQH_GPXZ", "GPXZ123321", "myapp", "plain", ""),
        # client.service.query(sessionId, "cxSqlKHCJTJ_GPXZ", params, "", mqueryOption),
        # client.service.query(sessionId, "cxSqlKHCJTJ_GPXZ", params, "", mqueryOption2),  # takes 1 sec
    ]
    future = asyncio.gather(*tasks, return_exceptions=True)
    sessionId = []
    def set_sessionId(future):
        ans = future.result()

        sessionId.append(ans[0].sessionId)
        tasks = [

            client.service.query(sessionId, "cxSqlKHCJTJ_GPXZ", params, "", mqueryOption),
            client.service.query(sessionId, "cxSqlKHCJTJ_GPXZ", params, "", mqueryOption2),  # takes 1 sec
        ]
        future2 = asyncio.gather(*tasks, return_exceptions=True)
        future2.add_done_callback(handle_future)
        loop.run_until_complete(future2)
        return
    future.add_done_callback(set_sessionId)

    st = time.time()
    loop.run_until_complete(future)
    loop.run_until_complete(transport.session.close())
    print("time: %.2f" % (time.time() - st))
    print("result: %s" % result)
    print("")
    print("sessionId:{sessionId}".format(sessionId=sessionId))
    return result





if __name__ == '__main__':
    print("")
    run_async()

