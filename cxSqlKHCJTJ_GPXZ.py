import zeep
import pandas as pd
wsdl = 'http://10.21.2.75:8080/service/LBEBusiness?wsdl'
client = zeep.Client(wsdl=wsdl)
# ns0:loginResult(message: xsd:string, result: xsd:int, sessionId: xsd:string)
sessionId = client.service.login("ZXQH_GPXZ", "GPXZ123321", "myapp", "plain", "")
print(client.service.login("ZXQH_GPXZ", "GPXZ123321", "myapp", "plain", ""))
factory = client.type_factory('ns0')
temp = factory.lbParameter(name='test', value='test')
print(temp)
# user = factory.User(id=1, name='John')
# order = factory.Order(number='1234', price=99)
string_type = client.get_type('xsd:string')
lbParameter_type = client.get_type('ns0:lbParameter')
queryOption_type = client.get_type('ns0:queryOption')
'''		tmap.put("KSRQ", "2018-02-26");
		tmap.put("JSRQ", "2018-02-26");
		tmap.put("YYB", "1");
		tmap.put("TJFL", "0");'''
par_dict = {"KSRQ":"2018-02-26", "JSRQ": "2018-02-26", "YYB": "30", "TJFL": "0", "KHH": "0000050067"}
par_dict = {"KSRQ":"2018-11-13",
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
batchNo=1
batchSize=3000
mqueryOption = queryOption_type(batchNo=batchNo, batchSize=batchSize, queryCount=True, valueOption=valueOption)


ans = client.service.query(sessionId.sessionId, "cxSqlKHCJTJ_GPXZ", params, "", mqueryOption)
print(ans)
while((ans.result>0) & ans.hasMore):
    batchNo += 1
    print('batchNo:{batchNo}'.format(batchNo=batchNo))

    mqueryOption = queryOption_type(batchNo=batchNo, batchSize=batchSize, queryCount=True, valueOption=valueOption)
    ans = client.service.query(sessionId.sessionId, "cxSqlKHCJTJ_GPXZ", params, "", mqueryOption)
    # print(ans)
    print('batchNo:{batchNo}'.format(batchNo=batchNo))

print(client.service.logout(sessionId.sessionId))
