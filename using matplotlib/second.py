import csv
from collections import Counter
from matplotlib import pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')
plt.title('Wine Servings in various Countries')
with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    country= list()
    beer_servings = list()
    sprit_servings = list()
    wine_servings = list()
    total_litres_of_pure_alcohol =list()

    for row in csv_reader:
            country.append(row['country'])
            beer_servings.append(float(row['beer_servings']))
            sprit_servings.append(float(row['spirit_servings']))
            wine_servings.append(float(row['wine_servings']))
            total_litres_of_pure_alcohol.append(float(row['total_litres_of_pure_alcohol']))

x_index = np.arange(len(country))
width = 0.25

plt.bar(x_index-width,beer_servings,width=width,label='Beer')
plt.bar(x_index,sprit_servings,width=width,label='Spirit')
plt.bar(x_index+width,wine_servings,width=width,label='Wine')
plt.bar(x_index+2*width,total_litres_of_pure_alcohol,width=width,label='total pure consumption alcohol in litres')
plt.legend()

plt.ylabel('Servings',fontsize=20)
plt.xlabel('Countries',fontsize=20)


plt.yticks(fontsize=8)
plt.xticks(ticks=x_index,labels=country,rotation=45,fontsize=8)

plt.grid(True)

plt.tight_layout()

#plt.savefig('plot.png')

plt.show()