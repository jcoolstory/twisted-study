from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

root = File('requesthandler.py')
root.putChild("doc", File('C:\\work\\jcool\\python\\twisted-study\\ex04\\webecho.py'))
root.putChild("logs", File("static_dispatch.py"))
factory = Site(root)
reactor.listenTCP(8000, factory)
reactor.run()

