from twisted.internet import reactor
from twisted.web.client import downloadPage
import sys

def printError(failure):
    print (sys.stderr, failure)

def stop(result):
    reactor.stop()

if len(sys.argv) != 3:
    exit(1)

d = downloadPage(sys.argv[1].encode(), sys.argv[2].encode())

#d.addErrback(printError)
#d.addBoth(stop)

reactor.run()
