from twisted.internet import reactor, protocol

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write(b"Hello, world!")

    def dataReceived(self, data):
        print("Server said:", data)
        self.transport.loseConnection()

class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, conenctor, reason):
        print("Connection failed.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost")
        print(reason)
        reactor.stop()

reactor.connectTCP("localhost", 8000, EchoFactory())
reactor.run()


