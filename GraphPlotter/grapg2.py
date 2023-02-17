import matplotlib.pyplot as plt

import random

x = [1, 2, 3, 4, 5]


y = [10, 11, 23, 36, 4]


tick_label = ['one', 'two', 'three', 'four', 'five']

plt.bar(x, y, tick_label=tick_label, width=0.8, color=['red', 'blue'])

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Demo Graph - Bar Chart')
plt.show()
