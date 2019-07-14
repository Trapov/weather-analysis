import csv
import numpy as np
import datetime as dt
import collections

a = []

with open('2011-2019.Orenburg.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f,  delimiter=';')
    for row in reader:
        if row["T"] and row["Time"] and row["U"]:
            ti = dt.datetime.strptime(row["Time"], '%d.%m.%Y %H:%M')
            a.append([ti, float(row["T"]), float(row["U"])])

narray = np.flip(np.array(a))

import matplotlib.pyplot as plt

f, temps, dates = narray.T

fig, ax = plt.subplots(nrows=1, ncols=2)

ax[0].bar(dates.astype(dt.datetime), f.astype('float'))
ax[0].set(xlabel='Date', title='Влажность')

ax[1].plot(dates.astype(dt.datetime), temps.astype('float'))
ax[1].set(xlabel='Date', ylabel='Temp (Cel)', title='Температура')

plt.grid()
plt.show()