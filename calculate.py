#! /usr/bin/env python
# -*- coding=utf-8 -*-

import itertools
import numpy as np


#list中4个数分别代表 x,y,z,e的系数,共10组
a_1 = [1.0, 1.0, 1.0, 1.0]
a_2 = [1.0, 2.0, 1.0, 1.0]
a_3 = [1.0, 1.0, 2.0, 1.0]
a_4 = [10.0, 7.0, 9.0, 6.0]
a_5 = [16.0, 18.0, 5.0, 7.0]
# a_6 = [361.35, 180.58, 56.72, 139.24]
# a_7 = [1603.53, 429.72, 204.73, 428.95]
# a_8 = [2075.72, 316.24, 414.48, 445.22]
# a_9 = [1482.32, 13.12, 558.68, 229.09]
# a_10 = [2227.56, 15.94, 1380.39, 378.44]

#list中4个数分别代表等号右边的值,共10组与a对应
b_1 = 120.0
b_2 = 180.0
b_3 = 220.0
b_4 = 3000.0
b_5 = 4500.0
# b_6 = -60.82
# b_7 = -62.63
# b_8 = -1.75
# b_9 = 37.52
# b_10 = 38.28

#方程
f_1 = [a_1, b_1]
f_2 = [a_2, b_2]
f_3 = [a_3, b_3]
f_4 = [a_4, b_4]
f_5 = [a_5, b_5]
# f_6 = [a_6, b_6]
# f_7 = [a_7, b_7]
# f_8 = [a_8, b_8]
# f_9 = [a_9, b_9]
# f_10 = [a_10, b_10]


def get_result(f_1, f_2, f_3, f_4):
    a = np.array([f_1[0],f_2[0],f_3[0],f_4[0]])
    b = np.array([f_1[1],f_2[1],f_3[1],f_4[1]])
    result = np.linalg.solve(a,b)
    #if float(result[0]) > 0:
    print(result)
    #print(np.dot(a,result))



c = list(itertools.combinations([f_1,f_2,f_3,f_4,f_5],4))

print(len(c))
for array in c:
    get_result(array[0],array[1],array[2],array[3])

