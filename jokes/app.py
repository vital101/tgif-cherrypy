from jinja2 import Environment, FileSystemLoader
import cherrypy, random

env = Environment(loader=FileSystemLoader("templates"))

class Joke(object):
    @cherrypy.expose
    def index(self):
        jokes = [
            "Why did the football coach go to the bank? To get his quarter back.",
            "Why can't a leopard hide? He's always spotted.",
            "Air used to be free at the gas station, now it costs 2.50. You want to know why? Inflation.",
            "Did you hear about the claustrophobic astronaut? He just wanted a bit more space.",
            "Why did the orange lose the race? It ran out of juice.",
            "How you fix a broken pumpkin? With a pumpkin patch."
        ]
        tmpl = env.get_template("jokes.html")
        return tmpl.render(joke=random.choice(jokes))