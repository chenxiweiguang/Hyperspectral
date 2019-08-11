#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:duwujun

fileName= '30mA-2.64V.hdr'
fileinfo =[]
with open(fileName, 'r') as fo:
    # tline=fo.readlines()
    # w=tline[1].strip('samples =')
    # h=tline[2].strip('lines = ')
    # b=tline[3].strip('bands = ')
    # lamda=tline[11].strip('wavelength = ')
    # print(w,h,b,lamda,tline)
    for line in fo.readlines():  # 依次读取每行
        line = line.strip(',\n')
        fileinfo.append(line)
    cloumn=fileinfo[1].strip('samples =')
    row=fileinfo[2].strip('lines = ')
    band=fileinfo[3].strip('bands = ')
    lamda=fileinfo[12:-2]
    print(cloumn,row,band,lamda)
