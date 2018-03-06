import pandas as pd
import matplotlib.pyplot as plt
# Create a Pandas dataframe from some data.
df = pd.DataFrame({'Numbers': [1010, 2020, 3030, 2020, 1515, 3030, 4545],
                   'Percentage': [.1, .2, .33, .25, .5, .75, .45],
                   })
test_df = df
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

fig, axes = plt.subplots(nrows=2, ncols=1, )
fig.set_figheight(4)
fig.set_figwidth(6)

plot1 = test_df[['Numbers', 'Percentage']].plot(
    x='Numbers', linestyle='-', marker='o', ax=axes[0])
plot2 = test_df[['Numbers', 'Percentage']].plot(
    x='Numbers', linestyle='-', marker='o', ax=axes[1])
df = pd.DataFrame({'Numbers': [1010, 2020, 3030, 2020, 1515, 3030, 4545],
                   'Percentage': [.1, .21, .1, .215, .51, .715, .415],
                   })
test_df = df
fig2, axes = plt.subplots(nrows=2, ncols=1, )
fig2.set_figheight(4)
fig2.set_figwidth(6)

plot1 = test_df[['Numbers', 'Percentage']].plot(
    x='Numbers', linestyle='-', marker='o', ax=axes[0])
plot2 = test_df[['Numbers', 'Percentage']].plot(
    x='Numbers', linestyle='-', marker='o', ax=axes[1])
from matplotlib.backends.backend_pdf import PdfPages

# plot1 = plotGraph(tempDLstats, tempDLlabels)
# plot2 = plotGraph(tempDLstats_1, tempDLlabels_1)
# plot3 = plotGraph(tempDLstats_2, tempDLlabels_2)

pp = PdfPages('foo2.pdf')
pp.savefig(fig)
pp.savefig(fig2)

pp.close()

import datetime
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

with PdfPages('multipage_pdf.pdf') as pdf:
    plt.figure(figsize=(3, 3))
    plt.plot(range(7), [3, 1, 4, 1, 5, 9, 2], 'r-o')
    plt.title('Page One')
    pdf.savefig()  # saves the current figure into a pdf page
    plt.close()

    # plt.rc('text', usetex=True)
    plt.figure(figsize=(8, 6))
    x = np.arange(0, 5, 0.1)
    plt.plot(x, np.sin(x), 'b-')
    plt.title('Page Two')
    pdf.savefig()
    plt.close()
    #
    # plt.rc('text', usetex=False)
    fig = plt.figure(figsize=(4, 5))
    plt.plot(x, x*x, 'ko')
    plt.title('Page Three')
    pdf.savefig(fig)  # or you can pass a Figure object to pdf.savefig
    plt.close()
    #
    # # We can also set the file's metadata via the PdfPages object:
    d = pdf.infodict()
    d['Title'] = 'Multipage PDF Example'
    d['Author'] = u'Jouni K. Sepp\xe4nen'
    d['Subject'] = 'How to create a multipage pdf file and set its metadata'
    d['Keywords'] = 'PdfPages multipage keywords author title subject'
    d['CreationDate'] = datetime.datetime(2009, 11, 13)
    d['ModDate'] = datetime.datetime.today()


import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.image as mimage
from matplotlib.backends.backend_pdf import PdfPages

_img = mimage.imread('test.jpg')

pdf = PdfPages( 'test.pdf' )
gs = gridspec.GridSpec(2, 4, top=1., bottom=0., right=1., left=0., hspace=0.,
        wspace=0.)

for g in gs:
    ax = plt.subplot(g)
    ax.imshow(_img)
    ax.set_xticks([])
    ax.set_yticks([])
#    ax.set_aspect('auto')

pdf.savefig()
pdf.close()
