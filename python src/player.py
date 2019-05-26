from settings import Settings
from map_mod import Map
import socket
import json
class Player(object):
	def __init__(self, coords, index):
		self.index_value = index
		self.coords = coords
		self.destination = None
		self.speed = 0
		

if __name__ == '__main__':
	play = Player((23,54))