#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import csv		
import numpy as np
import os 
import sys

typeIndex = 0  # herhangi bir data setindeki ic degisimler
index = 0      # herhangi bir data setindeki dosya degisimler
saveIndex = 0  # kaydedilecek yerdeki dosya indis
dataIndex = 0  # data seti indisi
dataEnd = 0    # herhangi bir data setindeki datanin bitme durumu 


	
readPath  = '/home/nvidia/Downloads/GTSRB_Final_Training_Images/GTSRB/Final_Training/Images/'+'%05d'%dataIndex+'/'
writePath = '/home/nvidia/Downloads/GTSRB_Final_Training_Images/GTSRB/Final_Training/Images/regularly/'

filep = file(writePath+'data.csv', "w+")
filep.write('FileName,ClassId\n')
		
while dataIndex !=43:

	if ( dataEnd == 2 ):

		typeIndex = 0
		dataEnd = 0
		index = 0
		dataIndex = dataIndex + 1
		
		readPath  = '/home/nvidia/Downloads/GTSRB_Final_Training_Images/GTSRB/Final_Training/Images/'+'%05d'%dataIndex+'/'

	dname = readPath+'%05d'%typeIndex+'_'+'%05d'%index+'.ppm'

	print dname

	if os.path.exists(dname):

		
		fname = writePath+'%05d.ppm'%saveIndex
		line = fname+ ',' + str(dataIndex)+ '\n'
		filep.write(line)
		img = cv2.imread(dname,1)
		img = cv2.resize(img, (48, 48))
		cv2.imwrite(fname,img)
		index = index + 1
		saveIndex = saveIndex + 1
		dataEnd = 0
	else:
		index = 0
		dataEnd = dataEnd + 1
		typeIndex = typeIndex + 1 
	
