from twisted.internet import reactor
from twisted.web import http

class MyRequestHandler(http.Request):

    resources = {
            '/' : '<h1>Home</h1>Home page',
            '/about':'<h1>About</h1>All about me',
            }

    def process(self):
        self.setHeader('Content-Type', 'text/html')
        path = self.path.decode('utf-8')
        if path in self.resources.keys():
            self.write(self.resources[path].encode())

        else :
            self.setResponseCode(http.NOT_FOUND)
            self.write(b"<h1>Not Found</h1>Sorry, no souch response.")

        self.finish()

class MyHTTP(http.HTTPChannel):
    requestFactory = MyRequestHandler

class MyHTTPFactory(http.HTTPFactory) :
    def buildProtocol(self, addr):
        return MyHTTP()

reactor.listenTCP(8000, MyHTTPFactory())
reactor.run()
