# import pandas as pd
#
# # Create a Pandas dataframe from the data.
# df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})
#
# # Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter('期货公司排名.xlsx', engine='xlsxwriter')
#
# # Convert the dataframe to an XlsxWriter Excel object.
# df.to_excel(writer, sheet_name='Sheet1')
#
# # Close the Pandas Excel writer and output the Excel file.
# writer.save()
#
import pandas as pd

# Create a Pandas dataframe from the data.
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter objects from the dataframe writer object.
# workbook  = writer.book
# worksheet = writer.sheets['Sheet1']
writer.save()

import xlrd
import xlsxwriter

from os.path import expanduser
home = expanduser("~")

# this writes test data to an excel file
# wb = xlsxwriter.Workbook("pandas_simple.xlsx")
# sheet1 = wb.add_worksheet()
# for row in range(10):
#     for col in range(20):
#         sheet1.write(row, col, "test ({}, {})".format(row, col))
# wb.close()

# open the file for reading
wbRD = xlrd.open_workbook("期货公司排名.xlsx")
sheets = wbRD.sheets()

# open the same file for writing (just don't write yet)
wb = xlsxwriter.Workbook("pandas_simple.xlsx")

# run through the sheets and store sheets in workbook
# this still doesn't write to the file yet
for sheet in sheets: # write data from old file
    newSheet = wb.add_worksheet(sheet.name)
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            newSheet.write(row, col, sheet.cell(row, col).value)
sheet2 = wb.add_worksheet('sheet2')
for row in range(10, 20): # write NEW data
    for col in range(20):
        sheet2.write(row, col, "test ({}, {})".format(row, col))
wb.close() # THIS writes
