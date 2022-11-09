from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        dict_toml=toml.loads(content)
        thename = dict_toml["tool"]["poetry"]["name"]
        thedescript = dict_toml["tool"]["poetry"]["description"]
        thedependenc = dict_toml["tool"]["poetry"]["dependencies"]
        the_dev_dependenc = dict_toml["tool"]["poetry"]["dev-dependencies"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(thename, thedescript, thedependenc, the_dev_dependenc)
