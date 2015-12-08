import csv
import os
from os.path import normpath, join, dirname

import matplotlib.pyplot as plt

appdir = dirname(os.getcwd())
source = normpath(join(appdir, 'data/data.csv'))
target = normpath(join(appdir, 'data/example01.png'))

y = []
# with open(source) as my_file:
#     y = my_file.readlines()

with open(source) as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        y = row

plt.plot(y)
plt.show()
plt.savefig(target)
