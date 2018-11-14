import pandas as pd
import os

import math
import pandas as pd

def sum_ins_table(temp_sum=None):
    start_col = 1
    end_col = 3
    ans = []
    for index in range(3):

        first_df = temp_sum.loc[:, start_col:end_col]
        first_df.columns = ['期货公司会员简称', '成交量', '比上交易日增减']
        # first_df['成交量'].astype(float)
        # first_df['比上交易日增减'].astype(float)
        # first_df[['成交量', '比上交易日增减']] = first_df[['成交量', '比上交易日增减']].astype(float, copy=True)
        # print(first_df['比上交易日增减'])

        first_df['成交量'] = first_df['成交量'].astype(float, copy=False)
        first_df['比上交易日增减'] = first_df['比上交易日增减'].astype(float, copy=False)
        # first_df.rename(columns=['期货公司会员简称', '成交量', '比上交易日增减'], inplace=True)
        first_ans = first_df.groupby(['期货公司会员简称', ])['成交量', '比上交易日增减'].sum() \
            .sort_values(by=['成交量'], ascending=False).reset_index().head(20)
        # print(first_ans)
        ans.append(first_ans)
        start_col += 4
        end_col += 4
    return ans

def split_ins(df):
    temp_index = df.index[df[0].str.contains('商品名称', case=False)].tolist()
    index_length = len(temp_index)
    ans_list = []
    for id in range(index_length):
        ins_df = None
        if id == index_length-1:
            ins_df = df[temp_index[id]:]
        else:
            ins_df = df[temp_index[id]:temp_index[id+1]]
        ins_df = ins_df.reset_index(drop=True)
        # print(ins_df)
        tb_index = ins_df.index[ins_df[0].str.contains('名次', case=False)].tolist()
        ins_header = ins_df[:(tb_index[0] - 1)]
        # 商品名称 ：铜                  2018-02-23
        ins_name = ins_header.iloc[0,0]
        import re
        x = re.split("：", ins_name)
        x = x[1].split()
        instrument = x[0]
        instrument_date = x[1]
        ins_name.split()
        temp_sum = None
        length = len(tb_index)
        for index, item in enumerate(tb_index):
            temp_df_1 = None
            if (index == length - 1):

                temp_df_1 = ins_df[(tb_index[index] + 1):-2]

            else:
                temp_df_1 = ins_df[(tb_index[index] + 1):(tb_index[index + 1] - 2)]
                # temp_df_1 = cu_df[(index + 1):(index+1 - 2)]
            if temp_sum is None:
                temp_sum = temp_df_1
            else:
                temp_sum = temp_sum.append(temp_df_1)
        print(temp_sum)
        print('-'*100 + instrument + '-'*100)
        rankings = sum_ins_table(temp_sum)
        print(rankings)
        print('-' * 100 + instrument + '-' * 100)
        ans = {}
        ans['instrument'] = instrument
        ans['date'] = instrument_date
        ans['ranking'] = rankings
        ans_list.append(ans)
    return ans_list

def main():
    a_file = '排名表2018-02-23.csv'
    df = pd.read_csv(a_file, names=range(12), encoding='gbk')

    ans = split_ins(df)
    test = ans[0]
    # print(test)
    test_df = test['ranking'][0]
    print(test_df)
    import matplotlib.pyplot as plt
    import matplotlib.pyplot as plt
    # coding:utf-8
    import matplotlib.pyplot as plt
    # plt.xticks(rotation=90)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # 有中文出现的情况，需要u'内容'
    # plt.figure()
    # #coding:utf-8
    # import matplotlib
    # matplotlib.use('qt4agg')
    # from matplotlib.font_manager import *
    # import matplotlib.pyplot as plt
    # #定义自定义字体，文件名从1.b查看系统中文字体中来
    # myfont = FontProperties(fname='/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc')
    # #解决负号'-'显示为方块的问题
    # matplotlib.rcParams['axes.unicode_minus']=False
    # plt.plot([-1,2,-5,3])
    # plt.title(u'中文',fontproperties=myfont)
    # plt.show()
    # plt.xticks(rotation=90)
    fig, axes = plt.subplots(nrows=2, ncols=1, )
    fig.set_figheight(6)
    fig.set_figwidth(8)
    # test_df['time'] = test_df['time'].apply(lambda x: x.strftime('%Y-%m-%d'))
    ax = test_df[['期货公司会员简称', '成交量']].plot(
        x='期货公司会员简称', linestyle='-', marker='o', ax=axes[0])
    ax2 = test_df[['期货公司会员简称', '比上交易日增减']].plot(
        x='期货公司会员简称', linestyle='-', marker='o', secondary_y=True, ax=axes[0])
    test_df[['期货公司会员简称', '成交量']].plot(x='期货公司会员简称', kind='bar'

                                      , sharex=True
                                      , ax=axes[1])
    axes[1].xaxis.set_tick_params(rotation=45)
    axes[1].set_xlabel("x-label", color="red")
    '''import numpy as np
    import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        p = plt.boxplot(np.random.normal(size=(10,3)))
        ax.set_xticklabels(list("abc"))
    
    [t.set_color(i) for (i,t) in
     zip(['red','green','blue'],ax.xaxis.get_ticklabels())]
    
    plt.show()'''
    for t in axes[1].xaxis.get_ticklabels():
        temp = t.get_text()
        temp = temp.strip()
        if temp == '中信期货':
            print(t.get_text())
    [t.set_color('red') for t in axes[1].xaxis.get_ticklabels()]
    # plt.setp(axes[1].get_xticklabels(), color="red")
    # [i.set_color("red") for i in plt.gca().get_xticklabels()]

    # for label in axes[1].get_xticklabels():
    #     label.set_fontproperties(ticks_font)
    #     ax.set_xticklabels(xlabels, rotation=45, rotation_mode="anchor")
    # axes[1].set_xticklabels(minor=False, rotation=45)
    # for k in ax.get_xmajorticklabels():
    #     if some-condition:
    #         k.set_color(any_colour_you_like)
    #
    # draw()



    fig.suptitle('Transaction Statistics', fontsize=14, fontweight='bold');
    import io
    from PIL import Image
    import xlsxwriter

    # from io import BytesIO
    # import matplotlib.pyplot as plt
    # imgdata = BytesIO()
    #
    # fig.savefig(imgdata, format="png")
    # imgdata.seek(0)
    # import io
    # from PIL import Image
    # import xlsxwriter
    #
    # workbook = xlsxwriter.Workbook('期货持仓分析报告.xlsx')
    # worksheet = workbook.add_worksheet("全市场成交统计")
    #
    # image_width = 140.0
    # image_height = 182.0
    #
    # cell_width = 64.0
    # cell_height = 20.0
    #
    # x_scale = cell_width/image_width * 10
    # y_scale = cell_height/image_height * 10
    #
    #
    #
    #
    #
    # # use with xlsxwriter
    # image_path = 'sales.png'
    # bound_width_height = (240, 240)
    # worksheet.insert_image('B5', image_path, {'image_data': imgdata,})
    # worksheet.insert_image('B40', image_path, {'image_data': imgdata,})
    # workbook.close()
    # plt.show()
    # plt.show()


    # a_file = '排名表2018-02-23.csv'
    # df = pd.read_csv(a_file,names=range(12), encoding='gbk')
    # # df = pd.read_excel(a_file, header=0, skip_blank_lines=True)
    # # print(df.nrows)
    # # df[df.col_name.str.startswith('abc')]
    # # np.array_split(df, 3)
    # # iloc[i]
    # # cu_df = df[0:165]
    # # print(cu_df)
    # split_ins(df)
    # print(df)
    # print(df.index.tolist())
    # print(df[0])
    # temp_index = df.index[df[0].str.contains('商品名称', case=False)].tolist()
    # print(temp_index)
    # cu_df = df[temp_index[0]:temp_index[1]]
    # print(cu_df)
    # cu_df_index = cu_df.index[cu_df[0].str.contains('名次', case=False)].tolist()
    # print(cu_df_index)
    # temp_row = df.iloc[cu_df_index[0]]
    # # <class 'list'>: ['名次', '期货公司会员简称', '成交量', '比上交易日增减', '名次', '期货公司会员简称', '持买单量',
    # # '比上交易日增减', '名次', '期货公司会员简称', '持卖单量', '比上交易日增减/变化']
    # print(df.iloc[cu_df_index[0]])
    # temp_sum = None
    # print(cu_df_index[-1])
    #
    # # for index, item in enumerate(sequence):
    # length = len(cu_df_index)
    # for index, item in enumerate(cu_df_index):
    #     temp_df_1 = None
    #     if (index == length-1):
    #         # len(cu_df)
    #         # temp_df_1 = cu_df[(index + 1):-2]
    #         temp_df_1 = cu_df[(cu_df_index[index] + 1):-2]
    #         break
    #     else:
    #         temp_df_1 = cu_df[(cu_df_index[index] + 1):(cu_df_index[index+1] - 2)]
    #         # temp_df_1 = cu_df[(index + 1):(index+1 - 2)]
    #     if temp_sum is None:
    #         temp_sum = temp_df_1
    #     else:
    #         temp_sum = temp_sum.append(temp_df_1)
    #
    # # temp_df_1 = cu_df[(cu_df_index[0]+1):(cu_df_index[1]-2)]
    # # temp_df_2 = cu_df[(cu_df_index[1]+1):(cu_df_index[2]-2)]
    # # temp_sum = temp_df_1.append(temp_df_2)
    # # temp_sum.rename(columns=temp_row, inplace=True)
    # print(temp_sum)
    # sum_ins_table(temp_sum)
    # # df.loc[:,[0]]
    # '''
    # old_names = ['$a', '$b', '$c', '$d', '$e']
    # new_names = ['a', 'b', 'c', 'd', 'e']
    # df.rename(columns=dict(zip(old_names, new_names)), inplace=True)'''
    # print(temp_sum.loc[:,1:3])
    # first_df = temp_sum.loc[:, 1:3]
    # first_df.columns = ['期货公司会员简称', '成交量', '比上交易日增减']
    # first_df['成交量'] = first_df['成交量'].astype(float)
    # first_df['比上交易日增减'] = first_df['比上交易日增减'].astype(float)
    # # first_df.rename(columns=['期货公司会员简称', '成交量', '比上交易日增减'], inplace=True)
    # first_ans = first_df.groupby(['期货公司会员简称', ])['成交量', '比上交易日增减'].sum()\
    #     .sort_values(by=['成交量'], ascending=False).reset_index().head(20)
    # # print(first_ans.head(20)  )
    #     # sort(['成交量',], ascending=[1,])
    # # df.loc[:,['c']]
    # # print(df[df.iloc[:,[0]].str.startswith('商品名称')])
    # print(df[df.iloc[:, 0].str.startswith('商品名称')])
    # temp = df.loc[:,[0]]
    # print(df.loc[:,[0]])
    # temp = df.loc[:, 0:1]
    # print(df.loc[:, 0].str.startswith('商品名称'))
    # for index, row in df.iterrows():  # 获取每行的index、row
    #     # print("index: {index}, row: {row}\n".format(index=index, row=row))
    #     print(row[0])
    #     # for col_name in df.columns:
    #     #     print(row[col_name])
    #
    # # for ix, col in df.iteritems():
    # #     print(ix)
    # #     print(col)
    #
    # print(df)
    # print("haha")
    return

if __name__ == "__main__":
    main()