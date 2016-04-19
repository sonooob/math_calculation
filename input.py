#! /usr/bin/env python
# -*- coding=utf-8 -*-
import xlrd as xl
import itertools
import numpy as np

#读取xls文件内容
fname = '4_14.xlsx'
data = xl.open_workbook(fname)
table = data.sheet_by_name('sheet')
nrows = table.nrows
ncols = table.ncols

f = []
for i in range(nrows):
    a_1 = table.row_values(i)[2:5]
    b_1 = float(table.row_values(i)[5:6][0])
    #b_1 = table.row_values(i)[4:5]
    f_1 = [a_1,b_1]
    f.append(f_1)
#print(f)

def get_result(f_1, f_2, f_3):
    a = np.array([f_1[0],f_2[0],f_3[0]])
    b = np.array([f_1[1],f_2[1],f_3[1]])
    result = np.linalg.solve(a,b)
    if float(result[0]) > 0 and float(result[1]) > 0 and float(result[2]) > 0:
        print(result)
    #print(np.dot(a,result))



c = list(itertools.combinations([f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8], f[9]], 3))


for array in c:
    #print(array[0][1])
    get_result(array[0],array[1],array[2])






