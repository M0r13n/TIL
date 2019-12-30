from twisted.internet import protocol, reactor
from twisted.internet.error import ConnectionDone


class Echo(protocol.Protocol):
    """
    protocols describe how to process network data asynchronously
    """

    def connectionMade(self):
        print("Client connected")

    def connectionLost(self, reason=ConnectionDone):
        print("Client disconnected. " + reason.getErrorMessage())

    def dataReceived(self, data):
        print("Recv: " + data.decode('utf-8'))
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    """
    For EVERY connection a new instance of the Echo protocol is created.
    This means that we can not persist data between connections in the protocol class.
    Data is therefore stored inside the Factory class.
    """

    def buildProtocol(self, addr):
        return Echo()


if __name__ == "__main__":
    # The reactor is the event loop that waits for events, demultiplexes them
    # and finally sends them to registered event handlers.
    # In this case we tell the reactor to send all packets that are TCP and coming to port 8000 to our EchoFactory.
    reactor.listenTCP(8000, EchoFactory())
    print("Echo server is listening on port 8000")
    reactor.run()

"""
The reactor essentially does the following logic:

while True:
    timeout = time_until_next_timed_event()  # define how long we wait for events
    events = wait_for_events(timeout) # wait and store all incoming events in a queue
    events += timed_events_until(now()) # after the timeout we process and dispatch every event one by one
    for event in events:
        event.process()
"""
