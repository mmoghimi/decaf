#!/usr/bin/env python

# This client demonstrates Thrift's connection and "oneway" asynchronous jobs
# Client connects to server host:port and calls 2 methods
# showCurrentTimestamp : which returns current time stamp from server
# asynchronousJob() : which calls a "oneway" method
#
# Osman Yuksel < yuxel {{|AT|}} sonsuzdongu |-| com >

host = "localhost"
port = 9090

import sys

# your gen-py dir
sys.path.append('gen-py')

# classify files
from classify import *
from classify.ttypes import *

# Thrift files 
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:

    # Init thrift connection and protocol handlers
    transport = TSocket.TSocket( host , port)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Set client to our classify
    client = decaf.Client(protocol)

    # Connect to server
    transport.open()

    # Run showCurrentTimestamp() method on server
    ret = client.classify(open("cat.jpg").read())
    print ret

    # Close connection
    transport.close()

except Thrift.TException, tx:
    print 'Something went wrong : %s' % (tx.message)
