import zeep

wsdl = 'http://10.21.2.75:8080/service/LBEBusiness?wsdl'
client = zeep.Client(wsdl=wsdl)
# ns0:loginResult(message: xsd:string, result: xsd:int, sessionId: xsd:string)
sessionId = client.service.login("ZXQH_GPXZ", "GPXZ123321", "myapp", "plain", "")
print(client.service.login("ZXQH_GPXZ", "GPXZ123321", "myapp", "plain", ""))
factory = client.type_factory('ns0')
# ns0:query(sessionId: xsd:string, objectName: xsd:string, params: ns0:lbParameter[], condition: xsd:string, queryOption: ns0:queryOption)
string_type = client.get_type('xsd:string')
lbParameter_type = client.get_type('ns0:lbParameter')
queryOption_type = client.get_type('ns0:queryOption')
# params_type = client.get_type('ns0:lbParameter[]')


params = []
# params: ns0:lbParameter[]
# order = order_type(number='1234', price=99)
'''tmap.put("KSRQ", "2017-11-09");
		tmap.put("JSRQ", "2018-02-26");
		tmap.put("KHH", "9000000063999");
		tmap.put("HYPZ", "IF");
		tmap.put("ZB", "0");
		tmap.put("ZQ", "1");'''
temp_lbParameter1 = lbParameter_type(name='KSRQ', value='2018-02-23')
temp_lbParameter2 = lbParameter_type(name='JSRQ', value='2018-02-23')
temp_lbParameter3 = lbParameter_type(name='TJLX', value='0')
temp_lbParameter4 = lbParameter_type(name='ZB', value='0')
temp_lbParameter5 = lbParameter_type(name='JYS', value='1')
temp_lbParameter6 = lbParameter_type(name='HYPZ', value='IF')
temp_lbParameter7 = lbParameter_type(name='PM', value='20')
params.append(temp_lbParameter1)
params.append(temp_lbParameter2)
params.append(temp_lbParameter3)
params.append(temp_lbParameter4)
params.append(temp_lbParameter5)
params.append(temp_lbParameter6)
params.append(temp_lbParameter7)
valueOption_type = client.get_type('ns0:valueOption')
valueOption = valueOption_type('VALUE')
# mqueryOption = queryOption_type(batchNo=1, batchSize=100, queryCount=False,)
mqueryOption = queryOption_type(batchNo=1, batchSize=100, queryCount=False, valueOption=valueOption)
# mqueryOption = queryOption_type(batchNo=1, batchSize=100, queryCount=False,)
# mqueryOption.setBatchNo(1)
# mqueryOption.setBatchSize(100)
# mqueryOption.setQueryCount(False)
# mqueryOption.setValueOption(valueOption_type.VALUE);

'''tmap.put("KSRQ", "2017-11-09");
		tmap.put("JSRQ", "2018-02-26");
		tmap.put("KHH", "9000000063999");
		tmap.put("HYPZ", "IF");
		tmap.put("ZB", "0");
		tmap.put("ZQ", "1");'''
# params = {"KSRQ":"2017-11-09", "JSRQ": "2018-02-26", "HYPZ":"IF", "ZB": "0", "ZQ":"1"}
'''mqueryOption.setBatchNo(1);
		mqueryOption.setBatchSize(100);
		mqueryOption.setQueryCount(false);
		mqueryOption.setValueOption(ValueOption.VALUE);'''
# mqueryOption = {'batchNo':'1', 'batchSize':'100', 'queryCount': False, 'valueOption':'1'}
# query.queryOption
ans = client.service.query(sessionId.sessionId, "CXSqlKHCJTJPM_GPXZ", params, "", mqueryOption)
print(ans)

print(client.service.logout(sessionId.sessionId))
