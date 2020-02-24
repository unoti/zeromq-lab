# Hello world client in Python
# Connects REQ socket to tcp://localhost:5555
# Sends "Hello" to server, expects "World" back.

import zmq

context = zmq.Context()

# Establish socket to talk to server.
print('Connecting to server')
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')

# Do 10 requests, waiting each time for a response.
for seq in range(10):
    print('Sending request %s...' % seq)
    socket.send(b'Hello')

    # Wait for reply.
    message = socket.recv()
    print('Received reply %s [%s]' % (seq, message))
