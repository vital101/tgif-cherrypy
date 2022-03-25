from apod.app import APOD
from jokes.app import Joke
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render(salutation='Hello', target='World')

cherrypy.tree.mount(APOD(), "/apod")
cherrypy.tree.mount(Joke(), "/joke")
cherrypy.tree.mount(Root(), "/")

cherrypy.engine.start()
cherrypy.engine.block()
