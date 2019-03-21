import sys

from twisted.internet import reactor
from twisted.web.client import Agent
from twisted.web.http_headers import Headers

def printHeaders(response):
    print('HTTP version:', response.version)
    print('Status code:', response.code)
    print('Status phrase:', response.phrase)
    print('Response headers')

    for header, value in response.headers.getAllRawHeaders():
        print( header.decode('utf-8'), value, type(value) )

def printError(failure):
    print (failure)

def stop(result):
    reactor.stop()

if len(sys.argv) != 2:
    print ("Usage: python print_metadata.py URL")
    exit(1)

agent = Agent(reactor)
headers = Headers({b'User-Agent' : [b'Twisted WebBot'],
                    b'Content-Type' : [b'text/x-greeting']})

d = agent.request(b'HEAD', sys.argv[1].encode(), headers=headers)
d.addCallbacks(printHeaders, printError)
d.addBoth(stop)

reactor.run()
