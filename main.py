# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 00:03:09 2021

@author: ianre
"""

from mnist import MNIST
import random
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

mndata = MNIST(dir_path + r'\training')
images, labels = mndata.load_training()


for i in range(10):    
    index = random.randrange(0, len(images))
    print(mndata.display(images[index]))

