import zeep
import pandas as pd
wsdl = 'http://10.21.2.75:8080/service/LBEBusiness?wsdl'
client = zeep.Client(wsdl=wsdl)
sessionId = client.service.login("ZXQH_GPXZ", "GPXZ123321", "myapp", "plain", "")
print(client.service.login("ZXQH_GPXZ", "GPXZ123321", "myapp", "plain", ""))
factory = client.type_factory('ns0')

# user = factory.User(id=1, name='John')
# order = factory.Order(number='1234', price=99)
string_type = client.get_type('xsd:string')
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
batchNo=1
batchSize=3000
mqueryOption = queryOption_type(batchNo=batchNo, batchSize=batchSize, queryCount=True, valueOption=valueOption)
ans = client.service.query(sessionId.sessionId, "cxSqlKHCJMX", params, "", mqueryOption)
print(ans)
while((ans.result>0) & ans.hasMore):
    batchNo += 1
    print('batchNo:{batchNo}'.format(batchNo=batchNo))

    mqueryOption = queryOption_type(batchNo=batchNo, batchSize=batchSize, queryCount=True, valueOption=valueOption)
    ans = client.service.query(sessionId.sessionId, "cxSqlKHCJTJ_GPXZ", params, "", mqueryOption)
    # print(ans)
    print('batchNo:{batchNo}'.format(batchNo=batchNo))

print(client.service.logout(sessionId.sessionId))
