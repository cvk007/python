from matplotlib import pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

ages_x = [25,26,27,28,29,30,31,32,33,34,35]

x_indexs = np.arange(len(ages_x))
width = 0.25

dev_y =[38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]

py_dev_y = [45372,48876,53850,57287,63016,65998,70003,70000,71496,75370,83640]

plt.bar(x_indexs-width,py_dev_y,width=width,color='#5ab451',linestyle='-.',linewidth=3,label='Python')

js_dev_y = [37810,43515,46823,49293,53437,56373,62375,66674,68745,68746,74583]

plt.bar(x_indexs,js_dev_y,label='JS',width=width,color='yellow',linestyle='--',linewidth=3)


plt.bar(x_indexs + width,dev_y,width=width,color='#444444',linestyle='--',label='All Devs')

plt.xlabel('Ages')
plt.ylabel('Salary')
plt.title('Median Salary of Python Developers (USD) by Age')

plt.xticks(ticks=x_indexs,labels=ages_x)
plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig('plot.png')

plt.show()