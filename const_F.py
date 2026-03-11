import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
fig, ax2 = plt.subplots()

ax1.plot([1, 2, 3, 4], [2.58621, 3.36497, 4.42991, 4.51476], "r.")
ax2.plot([1, 2, 3, 4, 5], [1.2211751, 7.204472, 5.687677, 4.878116, 4.540880], "b.")

ax1.set_title('C=-1.89')
ax2.set_title('C=-1.9')

ax1.grid()
ax2.grid()

plt.show()
