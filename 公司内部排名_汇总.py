import zeep
import pandas as pd

import os
import comtypes.client
import os

'''
#!/usr/bin/python 
dict={"a":"apple","b":"banana","o":"orange"} 

print "##########dict######################" 
for i in dict: 
        print "dict[%s]=" % i,dict[i] 

print "###########items#####################" 
for (k,v) in  dict.items(): 
        print "dict[%s]=" % k,v 

print "###########iteritems#################" 
for k,v in dict.iteritems(): 
        print "dict[%s]=" % k,v 

print "###########iterkeys,itervalues#######" 
for k,v in zip(dict.iterkeys(),dict.itervalues()): 
        print "dict[%s]=" % k,v 
'''


def excel_to_pdf(infile=None, outfile=None):
    cwd = os.getcwd()
    infile = os.path.join(os.path.abspath(cwd), infile)
    outfile = os.path.join(os.path.abspath(cwd), outfile)
    # infile = "C:/Users/niejn/PycharmProjects/scrapy_demo/期货统计排名_交易所.xlsx"
    # outfile = "C:/Users/niejn/PycharmProjects/scrapy_demo/test5.pdf"
    app = comtypes.client.CreateObject('Excel.Application')
    app.Visible = False
    doc = app.Workbooks.Open(infile, ReadOnly=False)
    doc.ExportAsFixedFormat(0, outfile, 1, 0)
    doc.Close()
    app.Quit()
    comtypes.CoUninitialize()
    return


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


def ranking_by_exchange():
    exchange_dict = {'1': '大连', '2': '上海', '3': '中金', '4': '郑州', }
    df_dict = {}
    for key in exchange_dict:
        print()

        par_dict = {"KSRQ": "2018-02-23", "JSRQ": "2018-02-23", 'TJLX': '2', 'ZB': '0',
                    'PM': '20'}
        par_dict['JYS'] = key
        lookout_str = 'CXSqlKHCJTJPM_GPXZ'
        records, meta = getData(par_dict, lookout_str)
        clean_records = []
        for a_record in records:
            clean_records.append(a_record.values)
        print(clean_records)
        tab_cols = meta
        df = pd.DataFrame(clean_records, columns=tab_cols)
        repl = lambda m: m[-1:]
        for x in df['客户姓名']:
            print("**" + x[-1:])
        df['客户姓名'] = ["**" + x[-1:] for x in df['客户姓名']]
        print(df['客户姓名'])
        df['客户姓名'].str.replace(r'[W]+', repl=repl)
        print(df['客户姓名'])
        # writer = pd.ExcelWriter('期货统计排名_交易所.xlsx', engine='xlsxwriter')
        print(df.columns)
        if '客户号' in df.columns:
            df = df.drop(['客户号', ], axis=1)
        df_dict[exchange_dict[key]] = df
    return df_dict
def ranking_by_ins():
    file = './config/douban.txt'
    ins_list = None
    with open(file, 'r') as srcFile:

        text = srcFile.readlines()
        print(text)
        # [x for x in a ifx%2==0]
        ins_list = [ins.strip()  for ins in text if '#' not in ins]


    df_dict = {}
    for key in ins_list:
        print()

        par_dict = {"KSRQ": "2018-02-23", "JSRQ": "2018-02-23", 'TJLX': '1', 'ZB': '0',
                    'PM': '20'}
        par_dict['HYPZ'] = key
        lookout_str = 'CXSqlKHCJTJPM_GPXZ'
        records, meta = getData(par_dict, lookout_str)
        clean_records = []
        for a_record in records:
            clean_records.append(a_record.values)
        print(clean_records)
        if not clean_records:
            continue
        tab_cols = meta
        df = pd.DataFrame(clean_records, columns=tab_cols)
        repl = lambda m: m[-1:]
        for x in df['客户姓名']:
            print("**" + x[-1:])
        df['客户姓名'] = ["**" + x[-1:] for x in df['客户姓名']]
        print(df['客户姓名'])
        # df['客户姓名'].str.replace(r'[W]+', repl=repl)
        # print(df['客户姓名'])
        # writer = pd.ExcelWriter('期货统计排名_交易所.xlsx', engine='xlsxwriter')
        print(df.columns)
        if '客户号' in df.columns:
            df = df.drop(['客户号', ], axis=1)
        df_dict[key] = df
    return df_dict

def ranking_by_total():

    ins_list = ['中信期货']



    df_dict = {}
    for key in ins_list:
        print()

        par_dict = {"KSRQ": "2018-02-23", "JSRQ": "2018-02-23", 'TJLX': '0', 'ZB': '0',
                    'PM': '20'}

        lookout_str = 'CXSqlKHCJTJPM_GPXZ'
        records, meta = getData(par_dict, lookout_str)
        clean_records = []
        for a_record in records:
            clean_records.append(a_record.values)
        print(clean_records)
        if not clean_records:
            continue
        tab_cols = meta
        df = pd.DataFrame(clean_records, columns=tab_cols)
        repl = lambda m: m[-1:]
        for x in df['客户姓名']:
            print("**" + x[-1:])
        df['客户姓名'] = ["**" + x[-1:] for x in df['客户姓名']]
        print(df['客户姓名'])
        # df['客户姓名'].str.replace(r'[W]+', repl=repl)
        # print(df['客户姓名'])
        # writer = pd.ExcelWriter('期货统计排名_交易所.xlsx', engine='xlsxwriter')
        print(df.columns)
        if '客户号' in df.columns:
            df = df.drop(['客户号', ], axis=1)
        df_dict[key] = df
    return df_dict

def save_pdf_xlsx_old(df_dict=None, by_volume=True, filename=None, header_name=None):
    writer = pd.ExcelWriter('{filename}.xlsx'.format(filename=filename), engine='xlsxwriter')
    workbook = writer.book

    # Add a header format.
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': False,

        'border': 1})
    header_format.set_align('center')
    header_format.set_align('vcenter')
    header_format.set_border(1)
    header_format.set_font_size(12)

    cell_format = workbook.add_format({
        'bold': False,
        'text_wrap': False,

        'border': 1})

    # cell_format.set_align()
    cell_format.set_align('center')
    cell_format.set_align('vcenter')
    cell_format.set_border(1)

    beg_row = 1
    worksheet2 = workbook.add_worksheet("期货排名")
    for key in df_dict:
        df = df_dict[key]
        # worksheet2 = workbook.add_worksheet("期货排名2")
        for index, row in df.iterrows():  # 获取每行的index、row
            for col_index, cell in enumerate(row):
                temp_row = index + 2 + beg_row
                worksheet2.write(temp_row, col_index, cell, cell_format)
        for col_num, value in enumerate(df.columns.values):
            temp_row = beg_row + 1
            worksheet2.write(temp_row, col_num, value, header_format)

        df_rows = df.shape[0]
        df_cols = df.shape[1]
        header_range = chr(65 + df_cols - 1)
        header_row = str(beg_row + 1)
        header_cmd_str = 'A{row}:{header_range}{row}'.format(header_range=header_range, row=header_row)
        temp_header_row = ''
        if by_volume:
            temp_header_row = '{exchange}客户成交量统计排名'.format(exchange=key)
        else:
            temp_header_row = '{exchange}客户成交金额统计排名'.format(exchange=key)
        worksheet2.merge_range(header_cmd_str, temp_header_row,
                               header_format)

        worksheet2.set_column('A:Z', 15, )
        worksheet2.set_row(beg_row, 30)
        beg_row += df_rows + 5

    writer.save()
    excel_to_pdf('{filename}.xlsx'.format(filename=filename), '{filename}.pdf'.format(filename=filename))
    return

def save_pdf_xlsx(df_dict=None, by_volume=True):
    writer = pd.ExcelWriter('期货统计排名_交易所.xlsx', engine='xlsxwriter')
    workbook = writer.book

    # Add a header format.
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': False,

        'border': 1})
    header_format.set_align('center')
    header_format.set_align('vcenter')
    header_format.set_border(1)
    header_format.set_font_size(12)

    cell_format = workbook.add_format({
        'bold': False,
        'text_wrap': False,

        'border': 1})

    # cell_format.set_align()
    cell_format.set_align('center')
    cell_format.set_align('vcenter')
    cell_format.set_border(1)

    beg_row = 1
    worksheet2 = workbook.add_worksheet("期货排名")
    for key in df_dict:
        df = df_dict[key]
        # worksheet2 = workbook.add_worksheet("期货排名2")
        for index, row in df.iterrows():  # 获取每行的index、row
            for col_index, cell in enumerate(row):
                temp_row = index + 2 + beg_row
                worksheet2.write(temp_row, col_index, cell, cell_format)
        for col_num, value in enumerate(df.columns.values):
            temp_row = beg_row + 1
            worksheet2.write(temp_row, col_num, value, header_format)

        df_rows = df.shape[0]
        df_cols = df.shape[1]
        header_range = chr(65 + df_cols - 1)
        header_row = str(beg_row+1)
        header_cmd_str = 'A{row}:{header_range}{row}'.format(header_range=header_range, row=header_row)
        temp_header_row = ''
        if by_volume:
            temp_header_row =  '{exchange}交易所客户成交量统计排名'.format(exchange=key)
        else:
            temp_header_row = '{exchange}交易所客户成交金额统计排名'.format(exchange=key)
        worksheet2.merge_range(header_cmd_str, temp_header_row,
                               header_format)


        worksheet2.set_column('A:Z', 15, )
        worksheet2.set_row(beg_row, 30)
        beg_row += df_rows+5


    writer.save()
    excel_to_pdf('期货统计排名_交易所.xlsx', '期货统计排名_交易所.pdf')
    return
def main():
    # df_dict = ranking_by_ins()
    df_dict = ranking_by_total()
    save_pdf_xlsx_old(df_dict, filename='期货统计排名_汇总')

    return


if __name__ == '__main__':
    main()