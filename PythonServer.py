#!/usr/bin/env python

# This server demonstrates Thrift's connection and "oneway" asynchronous jobs
# showCurrentTimestamp : which returns current time stamp from server
# asynchronousJob() : prints something, waits 10 secs and print another string
# 
# Osman Yuksel < yuxel {{|AT|}} sonsuzdongu |-| com >

port = 9090

import sys
# your gen-py dir
sys.path.append('gen-py')

import time

# Classify files
from classify import *
from classify.ttypes import *

# Thrift files
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

#*******************************************
import sys; sys.path.append("decaf")
from decaf.scripts.imagenet import DecafNet
import cStringIO as StringIO
import Image
import numpy as np
net = DecafNet('imagenet.decafnet.epoch90', 'imagenet.decafnet.meta')
from time import time as tic
#********************************************




# Server implementation
class ClassifyHandler:
    ## return current time stamp
    #def showCurrentTimestamp(self):
    #    timeStamp = time.time()
    #    return str(timeStamp)

    ## print something to string, wait 10 secs, than print something again
    #def asynchronousJob(self):
    #    print 'Assume that this work takes 10 seconds'
    #    time.sleep(10)
    #    print 'Job finished, but client didn\'t wait for 10 seconds'

    def classify(self, image):
        #return "notebook\nlaptop\ndesktop\ncomputer\nmodem\nscreen"
        print "--------------------------------------"
        print "input size:", len(image)
        start_time = tic()
        stream = StringIO.StringIO(image)
        img = np.asarray(Image.open(stream))
        scores = net.classify(img)
        #str(net.top_k_prediction(scores, 5))
        print "Hey"
        end_time = tic()
        print "time:", end_time-start_time
        res = "\n".join(net.top_k_prediction(scores, 5)[1])
        print "res:", res.replace("\n", " ")
        return res

# set handler to our implementation
handler = ClassifyHandler()

processor = decaf.Processor(handler)
transport = TSocket.TServerSocket(port = port)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# set server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print 'Starting server'
server.serve()
