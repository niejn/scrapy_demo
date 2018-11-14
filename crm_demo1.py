import zeep
import pandas as pd

def getData(par_dict={"KSRQ": "2018-02-26", "JSRQ": "2018-02-26", "YYB": "1", "TJFL": "0"},
            lookout_str='cxSqlKHCJTJ_GPXZ'):
    wsdl = 'http://10.21.2.75:8080/service/LBEBusiness?wsdl'
    client = zeep.Client(wsdl=wsdl)
    # ns0:loginResult(message: xsd:string, result: xsd:int, sessionId: xsd:string)
    sessionId = client.service.login("ZXQH_GPXZ", "GPXZ123321", "myapp", "plain", "")
    print(client.service.login("ZXQH_GPXZ", "GPXZ123321", "myapp", "plain", ""))
    factory = client.type_factory('ns0')
    string_type = client.get_type('xsd:string')
    lbParameter_type = client.get_type('ns0:lbParameter')
    queryOption_type = client.get_type('ns0:queryOption')
    '''		tmap.put("KSRQ", "2018-02-26");
    		tmap.put("JSRQ", "2018-02-26");
    		tmap.put("YYB", "1");
    		tmap.put("TJFL", "0");'''
    # par_dict = {"KSRQ": "2018-02-26", "JSRQ": "2018-02-26", "YYB": "1", "TJFL": "0"}
    params = []
    for key in par_dict:
        val = par_dict[key]
        temp_lbParameter = lbParameter_type(name=key, value=val)
        params.append(temp_lbParameter)

    valueOption_type = client.get_type('ns0:valueOption')
    valueOption = valueOption_type('VALUE')
    batchNo = 1
    batchSize = 3000
    ans_records = []
    mqueryOption = queryOption_type(batchNo=batchNo, batchSize=batchSize, queryCount=True, valueOption=valueOption)

    ans = client.service.query(sessionId.sessionId, lookout_str, params, "", mqueryOption)
    ans_records.extend(ans.records)
    print(ans)
    while ((ans.result > 0) & ans.hasMore):
        batchNo += 1
        print('batchNo:{batchNo}'.format(batchNo=batchNo))

        mqueryOption = queryOption_type(batchNo=batchNo, batchSize=batchSize, queryCount=True, valueOption=valueOption)
        ans = client.service.query(sessionId.sessionId, lookout_str, params, "", mqueryOption)
        ans_records.extend(ans.records)
        # print(ans)
        print('batchNo:{batchNo}'.format(batchNo=batchNo))

    print(client.service.logout(sessionId.sessionId))
    return ans_records


def main():
    # par_dict = {"KSRQ": "2017-11-09", "JSRQ": "2018-02-26", "KHH": "9000000063999", "HYPZ": "IF", "ZB": "0", "ZQ": "1"}
    # lookout_str = 'SqlCXKHCJQS'
    # par_dict = {"KSRQ": "2018-02-23", "JSRQ": "2018-02-23", "HYPZ": "cu", "ZB": "0", "ZQ": "0"}
    par_dict = {"KSRQ": "2018-02-01", "JSRQ": "2018-02-23", "ZB": "0", "ZQ": "0"}
    lookout_str = 'SqlGPXZGSSCQS'
    # par_dict = {"RQ": "2018-02-23", "HYPZ": "IF", "ZB": "0", "ZQ": "0"}
    # lookout_str = 'SqlGPXZSCZB'



    records = getData(par_dict, lookout_str)
    clean_records = []
    for a_record in records:
        clean_records.append(a_record.values)
    df = pd.DataFrame(clean_records,columns=['trade_type', 'time', 'sum',])
    df['time'] = pd.to_datetime(df['time'])
    df['sum'] = df['sum'].astype(float)
    df['sum'] = (df['sum'] * 2)  / df['sum'].max()
    # df['time'] = pd.to_datetime(df['time'])
    print(df)
    print(df['time'])
    df_market = df[df['trade_type'] == '市场']
    df_corpor = df[df['trade_type'] != '市场']
    print(df_market)
    print(df_corpor)
    join_df = df_market.set_index('time').join(df_corpor.set_index('time'),lsuffix='_market', rsuffix='_corpor')
    print(join_df['sum_market'])
    print()
    join_df.plot(subplots=True, figsize=(2, 1));
    ax = join_df.plot(subplots=False, figsize=(2, 1), logy=True)
    # ax.show()
    # plt.show()
    # df.plot(subplots=True, layout=(2, 3), figsize=(6, 6), sharex=False);
    # for a_record in records:
    #     trade_type = a_record.values[0]
    #     time_str = a_record.values[1]
    #     sum = a_record.values[2]
    return



if __name__ == '__main__':
    main()