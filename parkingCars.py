"""
随机停车问题：假设有n个车位，如果司机随意停车，则此n个车位平均能停几辆车？
解题思路：假设司机随机停到位置x，则剩下的车位位置是(0~x)和(x+1 ~ n)，可以用递归的思路来解决
"""

import random


def park(begin_pos, end_pos):
    if begin_pos + 1 > end_pos:
        return 0
    # elif begin_pos + 1 <= end_pos < begin_pos + 2:
    #     return 1
    else:
        rand_pos = random.uniform(begin_pos, end_pos-1)
        # print('{} {} {}'.format(begin_pos, end_pos,rand_pos))
        return 1+park(begin_pos, rand_pos) + park(rand_pos + 1, end_pos)


sum1 = 0
i = 0
while i <= 100000:
    sum1 += park(0, 5)
    i += 1
print(sum1 / i)
