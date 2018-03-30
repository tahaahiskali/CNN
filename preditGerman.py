#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, struct, array, time
from fcntl import ioctl

import cv2
import numpy as np
import threading
from enum import Enum


import os.path
from os.path import expanduser
import re
import json
from keras.models import model_from_json
	
# mname.json for model structure 
# mname.h5 for model weights
	
model_name = '/home/nvidia/k/marc_deep/ktrain/forGerman/agirliklar/cikis43noron/model_new'
jstr = json.loads(open(model_name+'.json').read())
model = model_from_json(jstr)
model.load_weights(model_name+'.h5')

image = cv2.imread('/home/nvidia/Downloads/GTSRB/Final_Test/Images/01000.ppm',1)
image = cv2.resize(image,(48,48))
image = np.array(image)
image = np.reshape(image, (1,48,48,3))
result = model.predict(image)
print(np.argmax(result))



		
