import matplotlib.pyplot as plt
import random

x = random.sample(range(1, 101), 20)
print(sorted(x))

y = random.sample(range(1, 101), 20)
print(sorted(y))

x1 = random.sample(range(1, 100), 20)
print(sorted(x1))

y1 = random.sample(range(1, 101), 20)
print(sorted(y1))

plt.plot(sorted(x), sorted(y), color="green", linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor="blue", markersize=12, label='Line 1')
plt.plot(sorted(x1), sorted(y1), label='Line 2')

plt.ylim(1, 101)
plt.xlim(1, 101)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Demo Graph - Customization')
plt.legend()

plt.show()
