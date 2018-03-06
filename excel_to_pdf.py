import os
import comtypes.client

SOURCE_DIR = 'C:/Users/IEUser/Documents/jscript/test/resources/root3'
TARGET_DIR = 'C:/Users/IEUser/Documents/jscript'

app = comtypes.client.CreateObject('Excel.Application')
app.Visible = False

infile = "C:/Users/niejn/PycharmProjects/scrapy_demo/期货统计排名_交易所.xlsx"
outfile = "C:/Users/niejn/PycharmProjects/scrapy_demo/test4.pdf"
# Open( FileName , UpdateLinks , ReadOnly , Format , Password , WriteResPassword ,
#  IgnoreReadOnlyRecommended , Origin , Delimiter , Editable , Notify , Converter , AddToMru , Local , CorruptLoad )
doc = app.Workbooks.Open(infile, ReadOnly=False)
'''expression.ExportAsFixedFormat(FixedFormat, OutputFileName, Intent, PrintRange, FromPage, 
ToPage, ColorAsBlack, IncludeBackground, IncludeDocumentProperties, 
IncludeStructureTags, UseISO19005_1, FixedFormatExtClass)'''
doc.ExportAsFixedFormat(0, outfile, 0, 0)
# 先删除同名文件
doc.Close()

app.Quit()
comtypes.CoUninitialize()