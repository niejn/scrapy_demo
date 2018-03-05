# coding: utf-8

import pandas as pd
# import shapefile
import os
# 网格编号    YMSS    HSLS    DDSJ
#os.chdir(r"K:\避洪转移文件")
xlsx = pd.ExcelFile("卫运河左堤风险数据 (2).xlsx")

for wk_sheet_name in xlsx.sheet_names:
    print(wk_sheet_name)
    df = pd.read_excel(xlsx.book,wk_sheet_name, engine='xlrd')
    # w = shapefile.Writer()
    # w.fields = [('DeletionFlag', 'C', 1, 0), ['YMSS', 'N', 12, 4], ['HSLS', 'N', 12, 4], ['DDSJ', 'N', 12, 4]]
    for i in range(len(df)):
        tmp_rec = df.iloc[i]
        vv = tmp_rec.get_values()
        tmp_lst = [round(i.item(),4)  for i in vv[1:]]
        # w.records.append(tmp_lst)
    # w.saveDbf(wk_sheet_name + ".dbf")