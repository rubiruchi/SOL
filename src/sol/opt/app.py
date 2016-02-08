import json
import uuid
from varnames import ALLOCATE_FLOW, ROUTE_ALL


class App:
    def __init__(self, pptc=None, resources=None, obj=None,
                 constraints=[ALLOCATE_FLOW, ROUTE_ALL], name=''):
        self.obj = obj
        self.pptc = pptc
        self.resources = resources
        self.name = name
        self.constraints = constraints
        if not self.name:
            self.name = uuid.UUID()

    def uses(self, resource):
        return resource in self.resources

    def getResourceNames(self):
        return self.resources.keys()

    def __repr__(self):
        return '<sol.App {}>'.format(self.name)

    @staticmethod
    def fromDict(dict):
        return App(dict['trafficClasses'], dict['resources'], dict['obj'],
                   name=dict['name'])

    @staticmethod
    def fromDescription(self, appString):
        return App.fromDict(json.loads(appString))
