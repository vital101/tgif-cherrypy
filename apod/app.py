from jinja2 import Environment, FileSystemLoader
import cherrypy, requests

env = Environment(loader=FileSystemLoader('templates'))

class APOD(object):
    cached_data = None

    @cherrypy.expose
    def index(self):
        title, explanation, image_url = self.__get_data()
        tmpl = env.get_template('apod.html')
        return tmpl.render(
            title=title,
            explanation=explanation,
            image_url=image_url
        )

    def __get_data(self):
        if not self.cached_data:
            res = requests.get("https://api.nasa.gov/planetary/apod?api_key=VIA9JEDe4WO5pISFYrhntLd8TvDGeWuLarHVs3gK")
            self.cached_data = res.json()
        return (
            self.cached_data["title"],
            self.cached_data["explanation"],
            self.cached_data["hdurl"]
        )