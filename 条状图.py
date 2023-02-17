import numpy as np
import matplotlib.pyplot as plt
'''画条状图'''
plt.rcParams['font.sans-serif']=['SimHei']  # 显示中文

X=np.arange(5)
Y1=np.array([10,13,5,45,12])
Y2=np.array([8,5,45,14,6])

plt.figure(1)
plt.bar(X-0.2,Y1,color='r',width=0.4,label='北京')
plt.bar(X+0.2,Y2,color='b',width=0.4,label='上海')
plt.xlabel('年份')
plt.ylabel('人口')
plt.title('城市-人口数据表')
plt.legend(loc='best') # 图例
# plt.text(X,Y1,'{}'.format(Y1))
for x,y1,y2 in zip(X,Y1,Y2):
    plt.text(x-0.2,y1,'{}'.format(y1),ha='center',va='bottom')
    plt.text(x+0.2, y2, '{}'.format(y2),ha='center',va='bottom')
plt.xticks(X,[2018,2019,2020,2021,2022])
y_ticks=np.arange(0,50,5)
plt.yticks(y_ticks,['{}(万人)'.format(y) for y in y_ticks])
ax=plt.gca()  # 边框不显示
ax.spines['right'].set_color(None)

ax.spines['top'].set_color(None)
plt.show()

























