#!/usr/bin/python 

import sys; sys.path.append("decaf")
from decaf.scripts.imagenet import DecafNet
import cStringIO as StringIO
import Image
import numpy as np
from time import time as tic

net = DecafNet('imagenet.decafnet.epoch90', 'imagenet.decafnet.meta')

start_time = tic()

#img = np.asarray(Image.open("cat.jpg"))
img_content = open("cat.jpg").read()
print len(img_content)
stream = StringIO.StringIO(img_content)
img = np.asarray(Image.open(stream))

scores = net.classify(img)
print net.top_k_prediction(scores, 5)
#scores = net.classify(img, center_only=True)

end_time = tic()
print "diff_time: %f"%(end_time - start_time)
