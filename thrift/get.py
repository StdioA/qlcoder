#!/usr/bin/env python

import sys
import glob
sys.path.append('gen-py')

from task7698 import Task
from task7698.ttypes import Auth, Type

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    # Make socket
    transport = TSocket.TSocket('121.201.63.168', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Task.Client(protocol)

    # Connect!
    transport.open()

    # Use your own username
    auth = Auth(username="StdioA", type=Type.GET_ANSWER)
    answer = client.getTaskInfo(auth)
    print answer
    
    # Close!
    transport.close()

if __name__ == '__main__':
    try:
        main()
    except Thrift.TException as tx:
        print('%s' % tx.message)
