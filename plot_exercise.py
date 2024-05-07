from typing import Counter

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

import os
from numpy.core.function_base import linspace

import csv
import pandas as pd



# ---------------------- Plots (+ plotstyle) --------------------- #

# print(plt.style.available)  ## to find available style
# plt.style.use('ggplot')  ## then you can use it
# # plt.xkcd()  ## cute comic style

# ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
#           36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]


# dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
#          78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]
# plt.bar(ages_x, dev_y, color='k', linestyle='--', label='All Devs')

# py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
#             84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]
# plt.plot(ages_x, py_dev_y, linewidth=2 ,label='Python')

# js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
#             78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]
# plt.plot(ages_x, js_dev_y, linewidth=2, label='Java')

# plt.xlabel('Ages')
# plt.ylabel('Median Salary')
# plt.title('Median Salary by Age')

# plt.legend()

# plt.grid(True)

# # plt.savefig('plot.png')
# plt.show()

# ------------------------- Bar (+ read csv_data) -------------------------- #

# print(plt.style.available)  ## to find available style
# plt.style.use('seaborn')  ## then you can use it
# plt.xkcd()  ## cute comic style


## read data

## 1. csv 
# with open('data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file) 

#     ## check the data:
#     # row = next(csv_reader) ## to see the first row of the 'csv_reader'
#     # print(row) 
#     # print(row['LanguagesWorkedWith']) # put the keyword
#     # print(row['LanguagesWorkedWith'].split(';'))


#     language_counter = Counter()
    
#     for row in csv_reader: ## How many times did the language show up?
#         language_counter.update(row['LanguagesWorkedWith'].split(';'))  # data box: language_counter

# ## split data
# languages = []
# popularity = []

# for item in language_counter.most_common(15):
#     languages.append(item[0])
#     popularity.append(item[1])

# languages.reverse()
# popularity.reverse()


## 2. panda
# data = pd.read_csv('data.csv')
# ids = data['Responder_id']
# lang_responses = data['LanguagesWorkedWith']

# language_counter = Counter()

# for response in lang_responses:
#     language_counter.update(response.split(';'))

# languages = []
# popularity = []

# for item in language_counter.most_common(15):
#     languages.append(item[0])
#     popularity.append(item[1])

# languages.reverse()
# popularity.reverse()

    
# ## plot

# plt.barh(languages, popularity)

# # plt.ylabel('Programming Languages')
# plt.xlabel('Number of Users')
# plt.title('Most Popular Programming Language')

# plt.tight_layout()

# plt.show()

# -------------------------- Pie Charts ----------------------------- #

# proportion = [30, 70]
# labels = ['30', '70']

# plt.pie(proportion)

# plt.title('My Pie Chart')
# plt.tight_layout()
# plt.show()

# -------------------------- Stack Plots (+ legend) --------------------------- #
# plt.style.use('seaborn') 

# minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ## 1,2,3 are in a team, we want to see the contribution of each player.
# player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
# player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
# player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

# labels = ['p1', 'p2', 'p3']
# colors = ['#6d904f', '#fc4f30', '#008fd5']

# # plt.pie([1,1,1], labels=["Player 1", "Player2", "Player3"])
# plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

# plt.legend(loc='upper left')  # control the position of legend
# plt.tight_layout()
# plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f

# -------------------------- Scatter Plots (+ read csv_data + colormap,colorbar) -------------------------- #
# plt.style.use('seaborn') 

# data = pd.read_csv('2019-05-31-data.csv')
# view_count = data['view_count']
# likes = data['likes']
# ratio = data['ratio']

# ## marker='X', edgecolor='black', linewidths=1, alpha=0.75
# ## colormap
# plt.scatter(view_count, likes, s=100, c=ratio, cmap='summer' )

# ## use log-scale to make the chart clearer (when only one data too big)
# plt.xscale('log')
# plt.yscale('log')

# plt.title('Trending YouTube Video')
# plt.xlabel('View Count')
# plt.ylabel('Total Likes')

# ## give labels to the colorbar
# cbar = plt.colorbar()
# cbar.set_label('LikeDislike Ratio')

# plt.show()

# -------------------- Plotting Time Series Data --------------------- #
# from datetime import datetime, timedelta
# from matplotlib import dates as mpl_dates

# # -----------
# # plt.gcf().autofmt_xdate() # rotate dates  gcf:get current figure

# # date_format = mpl_dates.DateFormatter('%b, %d, %Y') # change the form of date
# # plt.gca().xaxis.set_major_formatter(date_format)
# # -----------

# data = pd.read_csv('data2.csv')

# data['Date'] = pd.to_datetime(data['Date']) # to read date-data as date, not string
# data.sort_values('Date', inplace=True)  # inplace:direkt change the data, same as data=data.sort('Date')

# price_date = data['Date']
# price_close = data['Close']


# plt.plot_date(price_date, price_close, linestyle='solid')


# plt.xlabel('Datetime')
# plt.ylabel('Close')
# plt.gcf().autofmt_xdate() # rotate dates  gcf:get current figure

# plt.legend()

# plt.show()

# -------------------------Plotting Live Data in Real-Time (not finished) ----------------------------- #
# import random
# from itertools import count
# from matplotlib.animation import FuncAnimation

# plt.style.use('fivethirtyeight')

# x_vals = []
# y_vals = []

# index = count()

# def animate(i):
#     x_vals.append(next(index))
#     y_vals.append(random.randint(0,5))

#     plt.cla()  # change in one figure
#     plt.plot(x_vals, y_vals)

# ani = FuncAnimation(plt.gcf(), animate, interval=100)

# plt.tight_layout() # to add some automatic padding to our plot
# plt.show()

# -------------------------- Subplot (+ split figure) -------------------------------- #
# plt.style.use('seaborn')
# # plt.gcf()
# # plt.gca()

# # plt = Plot()  # stateful

# data = pd.read_csv('data3.csv')

# Ages = data['Age']
# dev_salaries = data['All_Devs']
# py_salaries = data['Python']
# js_salaries = data['JavaScript']

# fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)  # here we use 'ax' instead of 'plt.-Object'
#                                                   # and split our figure

# ax1.plot(Ages, dev_salaries, linestyle='--', label = 'All Devs')

# ax2.plot(Ages, py_salaries, label = 'Python')
# ax2.plot(Ages, js_salaries, label = 'JavaScript')

# ax1.legend()
# ax1.set_title('Median Salary')
# ax1.set_xlabel('Ages')
# ax1.set_ylabel('Salary')

# ax2.legend()
# ax2.set_title('Median Salary')
# ax2.set_xlabel('Ages')
# ax2.set_ylabel('Salary')

# plt.tight_layout()

# plt.show()

# G:/3D_P/Data/2D/b/1.5.csv
# -------------------------- read file ------------------------------ #

# with open('G:/3D_P/plot/t.dat', 'r') as f:  ## open the file in textform
#     line = f.read().split('/n')
#     c1 = []
#     ## transform the text into data(number)
#     for i in line[:-1]:  ## to read from beginning to the end of the line
#         var = i.split(': ')
#         c1.append(float(var[0]))
# print (np.array(c1))

    


# plt.plot(simulation_time, crack_length, label='b=1.5')

# plt.xlabel('Time')
# plt.ylabel('Crack Length')

# plt.grid(True)
# plt.legend()

# plt.show()


# Define a list of font families to test
font_families = ['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']

# Define text to display for each font family
text = 'Hello!'

# Create a plot for each font family
for i, font_family in enumerate(font_families):
    plt.subplot(1, len(font_families), i+1)
    plt.text(0.5, 0.5, text, fontfamily=font_family, fontsize=12, ha='center')
    plt.title(font_family)
    plt.axis('off')  # Hide axis
    plt.tight_layout()

plt.show()


# #-------------multiple plot------------------
# print(plt.style.available) 
plt.style.use('ggplot')
params = {
"font.size": 12,     # 全局字号
'font.family':'STIXGeneral', # 全局字体
"figure.subplot.wspace":0.2, # 图-子图-宽度百分比
"figure.subplot.hspace":0.4, # 图-子图-高度百分比
"axes.spines.right":False,  # 坐标系-右侧线
"axes.spines.top":False,   # 坐标系-上侧线
"axes.titlesize":12,   # 坐标系-标题-字号
"axes.labelsize": 12,  # 坐标系-标签-字号
"legend.fontsize": 12,  # 图例-字号
"xtick.labelsize": 10,  # 刻度-标签-字号
"ytick.labelsize": 10,  # 刻度-标签-字号
"xtick.direction":'in',   # 刻度-方向
"ytick.direction":'in'  # 刻度-方向
}
mpl.rcParams.keys(params)

t_a = pd.read_csv('G:/3D_P/Data/2D/b/group0/data_all/1.5.csv')['time']
crack_length_a = pd.read_csv('G:/3D_P/Data/2D/b/group0/data_all/1.5.csv')['crack_len']
crack_tip_a = pd.read_csv('G:/3D_P/Data/2D/b/group0/data_all/1.5.csv')['crack_tip']

t_b = pd.read_csv('G:/3D_P/Data/2D/b/group0/data_all/2.5.csv')['time']
crack_length_b = pd.read_csv('G:/3D_P/Data/2D/b/group0/data_all/2.5.csv')['crack_len']

x_list = [t_a, t_b]
y_list = [crack_length_a, crack_length_b]




# for i in range(0,len(x_list)):
#     plt.plot(x_list[i],y_list[i])

# font = {'family': 'serif',
#         'color': 'black',
#         'weight': 'normal',
#         'size': 8,
#         }

# plt.xlabel('Cycles',fontdict=font)
# plt.ylabel(r'Crack length [L]',fontdict=font)

# plt.xticks(fontsize=8)
# plt.yticks(fontsize=8)

# # plt.legend()
# plt.grid(linestyle = "--")

# plt.show()

# lines.linewidth : 2.0

# patch.linewidth: 0.5
# patch.facecolor: blue
# patch.edgecolor: eeeeee
# patch.antialiased: True

# text.hinting_factor : 8

# mathtext.fontset : cm

# axes.facecolor: eeeeee
# axes.edgecolor: bcbcbc
# axes.grid : True
# axes.titlesize: x-large
# axes.labelsize: large
# axes.prop_cycle: cycler('color', ['348ABD', 'A60628', '7A68A6', '467821', 'D55E00', 'CC79A7', '56B4E9', '009E73', 'F0E442', '0072B2'])

# grid.color: b2b2b2
# grid.linestyle: --
# grid.linewidth: 0.5

# legend.fancybox: True

# xtick.direction: in
# ytick.direction: in