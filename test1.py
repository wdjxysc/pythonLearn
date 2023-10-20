import cherrypy
class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        # return "Hello World!"
        cherrypy.session['mystring'] = 'injoker'
        return "<h1>呵呵呵</h1>"
    index.exposed = True
    @cherrypy.expose
    def hello(self):
        return cherrypy.session['mystring']
    hello.exposed = True

if __name__ == '__main__':
 
    conf = {
        '/': {
            'tools.sessions.on': True,   # 在cherryPy中启用session
        }
    }
    print("hehe", end="?\n")
    cherrypy.quickstart(HelloWorld(), '/', conf)
    