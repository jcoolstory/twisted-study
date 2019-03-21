from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site

import cgi

class FormPage(Resource):
    isLeaf = True

    def render_GET(self, request):
        return b"""
<html>
<body>
<form method="POST">
<input name="form-field" type="text" />
<input type="submit" />
</form>
</body>
</html>
"""

    def render_POST(self, request):
        print(request.args)
        ret =  """
<html>
<body>You submiited: %s</body>
</html>
""" % (cgi.escape(request.args[b"form-field"][0].decode('utf-8')),)
        return ret.encode()

factory = Site(FormPage())
reactor.listenTCP(8000, factory)
reactor.run()




