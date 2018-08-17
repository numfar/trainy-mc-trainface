# -*- coding: utf-8 -*-
import re

class TrainStopp(object):

    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y

class Route(object):

    def __init__(self,name):
        self.name = name
        self.stops = []

class FileCoordinatesExtractor(object):

    def extract_route(self,filename):
        route = Route(filename)
        with open(filename,'r') as fileStream:
            for line in fileStream.readlines():
                cols = line.split(',')
                stop = TrainStopp(cols[0],int(cols[1]),int(cols[2]))
                route.stops.append(stop)
        return route