# Hello world server in Python
# Binds REP socket to tcp://*:5555
# Expects b'Hello' from client and replies with b'World'.

import time
import zmq


def run_app():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://*:5556')

    try:
        print('Starting server')
        while True:
            # Wait for next client request.
            message = socket.recv()
            print('Received request:', message)

            # Do some 'work'.
            time.sleep(1)

            # Send reply to client.
            socket.send(b'World')
    finally:
        socket.setsockopt(zmq.LINGER, 0) # Avoid hanging indefinitely
        socket.close()
        context.term() # Terminate context before terminating.

if __name__ == '__main__':
    run_app()