from twisted.internet.protocol import Factory
from twisted.internet import reactor, protocol
from twisted.internet.error import ConnectionDone


class QuoteProtocol(protocol.Protocol):

    def __init__(self, factory):
        self.factory = factory  # reference to parent factory

    def connectionMade(self):
        self.factory.numConnections += 1
        print("Client connected")

    def connectionLost(self, reason=ConnectionDone):
        self.factory.numConnections -= 1
        print("Client disconnected. " + reason.getErrorMessage())

    def dataReceived(self, data):
        print(f"{self.factory.numConnections} concurrent connections")
        print(f"Received {data.decode('utf-8')} {self.getQuote()}")
        self.transport.write(self.getQuote().encode('utf-8'))
        self.transport.write("\n".encode('utf-8'))

    def getQuote(self):
        return self.factory.quote

    def updateQuote(self, quote):
        self.factory.quote = quote


class QuoteFactory(Factory):
    numConnections = 0

    def __init__(self, quote="An apple a day keeps the doctor away"):
        self.quote = quote

    def buildProtocol(self, addr):
        return QuoteProtocol(self)


if __name__ == "__main__":
    reactor.listenTCP(8000, QuoteFactory())
    print("Start listening on port 8000")
    reactor.run()


"""
Can be rewritten like that
class QuoteFactory(Factory):
    numConnections = 0
    protocol = QuoteProtocol
    
    def __init__(self, quote="An apple a day keeps the doctor away"):
        self.quote = quote
"""
