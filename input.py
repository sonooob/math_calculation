#! /usr/bin/env python
# -*- coding=utf-8 -*-
import xlrd as xl
import itertools
import numpy as np

fname = '3.xlsx'
data = xl.open_workbook(fname)
table = data.sheet_by_name(u'按地类')
nrows = table.nrows
ncols = table.ncols

f = []
for i in range(2,nrows):
    a_1 = table.row_values(i)[0:4]
    b_1 = float(table.row_values(i)[6:7][0])
    #b_1 = table.row_values(i)[4:5]
    f_1 = [a_1,b_1]
    f.append(f_1)


def get_result(f_1, f_2, f_3, f_4):
    a = np.array([f_1[0],f_2[0],f_3[0],f_4[0]])
    b = np.array([f_1[1],f_2[1],f_3[1],f_4[1]])
    result = np.linalg.solve(a,b)
    if float(result[0]) > 0:
        print(result)
    #print(np.dot(a,result))



c = list(itertools.combinations([f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8],f[9]],4))


for array in c:
    #print(array[0][1])
    get_result(array[0],array[1],array[2],array[3])





