import zeep
import pandas as pd
def getData(par_dict = {"KSRQ": "2018-02-26", "JSRQ": "2018-02-26", "YYB": "1", "TJFL": "0"},
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
    batchSize = 100
    ans_records = []
    mqueryOption = queryOption_type(batchNo=batchNo, batchSize=batchSize, queryCount=True, valueOption=valueOption)

    ans = client.service.query(sessionId.sessionId, lookout_str, params, "", mqueryOption)
    ans_records.extend(ans.records)
    temp_meta = ans.metaData.colInfo
    print(temp_meta)
    ans_meta = [it['label'] for it in temp_meta]
    print(ans_meta)
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
    return ans_records, ans_meta

def sum_market():
    par_dict = {"KSRQ": "2018-01-01", "JSRQ": "2018-02-23", "ZB": "0", "ZQ": "0"}
    lookout_str = 'SqlGPXZGSSCQS'

    records = getData(par_dict, lookout_str)
    print(records)
    clean_records = []
    for a_record in records:
        clean_records.append(a_record.values)
    df = pd.DataFrame(clean_records, columns=['trade_type', 'time', 'sum', ])
    print(df.head())
    df['time'] = pd.to_datetime(df['time'])
    df['sum'] = df['sum'].astype(float)
    df['sum'] = df['sum'] / df['sum'].max()
    # df['sum'] = (df['sum'] * 100) / df['sum'].max


    df_market = df[df['trade_type'] == '市场']
    df_corpor = df[df['trade_type'] != '市场']

    join_df = df_market.set_index('time').join(df_corpor.set_index('time'), lsuffix='_market', rsuffix='_corpor')
    print(join_df['sum_market'])
    print()
    # join_df.plot(subplots=True, figsize=(10, 5));
    # join_df.plot(subplots=False, figsize=(10, 5), logy=True)
    return

def main():
    # test()
    # par_dict = {"KSRQ": "2017-11-09", "JSRQ": "2018-02-26", "KHH": "9000000063999", "HYPZ": "IF", "ZB": "0", "ZQ": "1"}
    # lookout_str = 'SqlCXKHCJQS'
    # par_dict = {"KSRQ": "2018-02-23", "JSRQ": "2018-02-23", "HYPZ": "cu", "ZB": "0", "ZQ": "0"}
    # par_dict = {"KSRQ": "2018-02-01", "JSRQ": "2018-02-23", "ZB": "0", "ZQ": "0", "TJFL":"0", "JYS":"1"}
    # par_dict = {"KSRQ": "2018-02-01", "JSRQ": "2018-02-23", "ZB": "0", "ZQ": "0", "TJFL":"1",}
    # lookout_str = 'SqlGPXZGSSCQS'
    # par_dict = {"RQ": "2018-02-23", "HYPZ": "IF", "ZB": "0", "ZQ": "0"}
    # lookout_str = 'SqlGPXZSCZB'


    # temp_lbParameter1 = lbParameter_type(name='KSRQ', value='2018-02-23')
    # temp_lbParameter2 = lbParameter_type(name='JSRQ', value='2018-02-23')
    # temp_lbParameter3 = lbParameter_type(name='TJLX', value='0')
    # temp_lbParameter4 = lbParameter_type(name='ZB', value='0')
    # temp_lbParameter5 = lbParameter_type(name='JYS', value='1')
    # temp_lbParameter6 = lbParameter_type(name='HYPZ', value='IF')
    # temp_lbParameter7 = lbParameter_type(name='PM', value='20')
    # 'TJLX':'0', 'ZB':'0', 'JYS':'1', 'HYPZ':'IF', 'PM':'20'
    # par_dict = {"KSRQ": "2018-02-23", "JSRQ": "2018-02-23", 'TJLX':'0', 'ZB':'0', 'JYS':'1', 'HYPZ':'IF', 'PM':'20'}
    par_dict = {"KSRQ": "2018-02-23", "JSRQ": "2018-02-23", 'TJLX': '0', 'ZB': '0',
                'PM': '20'}
    '''统计类型：TJLX   0|客户;1|品种;2|交易所; 
     指标：ZB  0|成交量;1|成交金额;
     交易所 JYS  1 大连;2|上海;3|中金;4|郑州;5|能源
     合约品种 HYPZ 
     开始日期  KSRQ
     结束日期  JSRQ
     排名前   PM
'''
    par_dict = {"KSRQ": "2018-02-23", "JSRQ": "2018-02-23", 'TJLX': '2', 'ZB': '0', 'JYS':'1',
                'PM': '20'}
    # 一．客户成交统计排名（CXSqlKHCJTJPM_GPXZ）
    lookout_str = 'CXSqlKHCJTJPM_GPXZ'

    records, meta = getData(par_dict, lookout_str)
    clean_records = []
    for a_record in records:
        clean_records.append(a_record.values)
    # df = pd.DataFrame(data)
    print(clean_records)
    tab_cols = meta
    # tab_cols = ['客户号', '客户姓名', '成交量', '成交金额', '排名', ]
    df = pd.DataFrame(clean_records, columns=tab_cols)
    repl = lambda m: m[-1:]
    for x in df['客户姓名']:
        print("**" + x[-1:])
    df['客户姓名'] = ["**" + x[-1:] for x in df['客户姓名']]

    print(df['客户姓名'])
    df['客户姓名'].str.replace(r'[W]+', repl = repl)
    print(df['客户姓名'])
    for index, row in df.iterrows():  # 获取每行的index、row
        print(index)
        print(row)
        for col_index, cell in enumerate(row):
            print(col_index)
            print(cell)
        for col_name in df.columns:
            print(row[col_name])
            pass
    # for a_record in records:
    #     trade_type = a_record.values[0]
    #     time_str = a_record.values[1]
    #     sum = a_record.values[2]
    return
'''IF
沪深300指数
TF
5年期国债
hc
热轧卷板
cu
铜
al
铝
ru
天然橡胶
ag
白银
bu
石油沥青
fu
燃料油
zn
锌
au
黄金
rb
螺纹钢
wr
线材
pb
铅
m
豆粕
s
大豆
jm
焦煤
jd
鲜鸡蛋
i
铁矿石
fb
中密度纤维板
bb
细木工板
pp
聚丙烯
c
黄玉米
y
豆油
l
线型低密度聚乙烯
p
棕榈油
v
聚氯乙烯
j
冶金焦炭
OI
菜籽油
RI
籼稻RI
WH
强麦WH
FG
玻璃
RS
油菜籽
RM
菜籽粕
TC
动力煤
JR
粳稻谷
CF
一号棉花
SR
白砂糖
TA
精对苯二甲酸
ME
甲醇
PM
普通小麦
IH
上证50指数
CS
棉二
ER
籼稻ER
RO
菜籽油
WS
强麦WS
WT
硬冬白小麦
GN
绿豆
b
黄大豆2号
a
黄大豆1号


 

 
 
 '''
if __name__ == '__main__':
    main()