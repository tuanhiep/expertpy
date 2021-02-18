# Function to multiply matrix1 to matrix2
from random import random
from time import time as timestamp
import matplotlib.pyplot as plt

from resource import getrusage as resource_usage, RUSAGE_SELF


def multi(matrix1, matrix2):
    res = [[0 for x in range(len(matrix2[0]))] for y in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                # resulted matrix
                res[i][j] += matrix1[i][k] * matrix2[k][j]
    return res


#
# x1 = [[2, 2],
#       [3, 4]]
# y1 = [[5, 6, 1],
#       [1, 3, 2]]
#
# print(multi(x1, y1))
# Sizes of the matrix
# sizes = [250, 500, 1000, 1500, 2000]
sizes = [25, 50]
total = [None] * len(sizes)
user = [None] * len(sizes)
sys = [None] * len(sizes)
count = 0
for size in sizes:
    m1 = [[random() for x in range(size)] for y in range(size)]
    m2 = [[random() for x in range(size)] for y in range(size)]
    start_time, start_resources = timestamp(), resource_usage(RUSAGE_SELF)
    m3 = multi(m1, m2)
    end_time, end_resources = timestamp(), resource_usage(RUSAGE_SELF)
    total[count] = end_time - start_time
    sys[count] = end_resources.ru_stime - start_resources.ru_stime
    user[count] = end_resources.ru_utime - start_resources.ru_utime
    count += 1
print(user)
print(sys)
print(total)



fig, ax = plt.subplots()
ax.set_prop_cycle(color=['red', 'green', 'blue'])
plt.plot(sizes, user)
plt.plot(sizes, sys)
plt.plot(sizes, total)
plt.legend(['user', 'system', 'total'], loc='upper left')

plt.show()
