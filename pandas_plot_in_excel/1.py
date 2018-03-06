# import matplotlib.pyplot as plt
# from cStringIO import StringIO
# imgdata = StringIO()
#
# fig, ax = plt.subplots()
#
# # Make your plot here referencing ax created before
# results.resid.hist(ax=ax)
#
# fig.savefig(imgdata)
#
# worksheet.insert_image(row, 0, imgdata)

#
# import matplotlib.pyplot as pltfrom PIL import Image
#
# file_in = "image.png"
# img = Image.open(file_in)
# file_out = 'test1.bmp'
# print len(img.split()) # test
# if len(img.split()) == 4:
#     # prevent IOError: cannot write mode RGBA as BMP
#     r, g, b, a = img.split()
#     img = Image.merge("RGB", (r, g, b))
#     img.save(file_out)
# else:
#     img.save(file_out)
#
# from xlwt import Workbook
# w = Workbook()
# ws = w.add_sheet('Image')
# ws.insert_bitmap(file_out, 0, 0)
# w.save('images.xls')
#
# from io import BytesIO
# import matplotlib.pyplot as plt
#
# imgdata = BytesIO()
# fig, ax = plt.subplots()
# results.resid.hist(ax=ax)
# fig.savefig(imgdata, format="png")
# imgdata.seek(0)
#
# worksheet.insert_image(
#     row, 0, "",
#     {'image_data': imgdata}
# )
#
# import xlrd
# import numpy as np
# file_location = "C:/Users/Rima/Desktop/apjl731data.xlsx"
# workbook = xlrd.open_workbook(file_location)
# first_sheet = workbook.sheet_by_index(0)
#
# x = [first_sheet.cell_value(i, 0) for i in range(first_sheet.ncols)]
# y = [first_sheet.cell_value(i, 1) for i in range(first_sheet.ncols)]
# yerr_pos = [first_sheet.cell_value(i, 2) for i in range(first_sheet.ncols)]
# yerr_neg = [first_sheet.cell_value(i, 3) for i in range(first_sheet.ncols)]
#
# yerr = [yerr_neg, yerr_pos]
#
# plt.errorbar(x,y,yerr,fmt='r^')
#
# plt.axis([0,5,0,5])
# plt.show()
#
# from xlwt import Workbook
# w = Workbook()
# ws = w.add_sheet('Image')
# ws.insert_bitmap(file_out, 0, 0)
# w.save('images.xls')
#
# import xlsxwriter
#
# book = xlsxwriter.Workbook('pict.xlsx')
# sheet = book.add_worksheet('demo')
# sheet.insert_image('D4', 'sales.png')
# book.close()