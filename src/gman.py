from src.coordinate import *

class Gman:
	def __init__(self, source, direction, destination):
		self.__source = source
		self.__direction = direction
		self.__destination = destination
		self.__power = 200
		self.__travelling_power = 10
		self.__turning_power = 5
		self.__distance_travelled = 0 
		self.__turns_taken = 0
		self.__relative_direction = []

	def get_source(self):
		return self.__source

	def set_source(self, source):
		self.__source = source

	def get_destination(self):
		return self.destination

	def set_destination(self, destination):
		self.__destination = destination

	def get_direction(self):
		return self.direction

	def set_direction(self, direction):
		self.__direction = direction

	def get_power(self):
		return self.power

	def set_power(self, power):
		self.__power = power

	def get_distance_travelled(self):
		return self.distance_travelled

	def set_distance_travelled(self, distance_travelled):
		self.__distance_travelled = distance_travelled

	def get_turns_taken(self):
		return self.turns_taken

	def set_turns_taken(self, turns_taken):
		self.__turns_taken = turns_taken

	def get_relative_direction(self):
		return self.__relative_direction

	# finds relative distance between source and destination
	def destination_direction_from_source(self):
		src_x = self.__source.get_x()
		src_y = self.__source.get_y()

		dest_x = self.__destination.get_x()
		dest_y = self.__destination.get_y()

		if (src_x == dest_x):
			self.__relative_direction.append(self.__direction)
		elif (src_x < dest_x):
			self.__relative_direction.append("E")
		else:
			self.__relative_direction.append("W")

		if (src_y == dest_y):
			self.__relative_direction.append(self.__direction)
		elif (src_y < dest_y):
			self.__relative_direction.append("N")
		else:
			self.__relative_direction.append("S")

	# calculate total turns g-man needs to take 
	def calculate_turns_taken(self):
		if (self.__direction != self.__relative_direction[0]):
			self.__turns_taken += 1

		if (self.__direction != self.__relative_direction[1]):
			self.__turns_taken += 1

	# calculate horizontal and vertical difference in distance between source and destination
	def calculate_distance_travelled(self):
		horizontal_diff = abs(int(self.__source.get_x()) - int(self.__destination.get_x()))

		vertical_diff = abs(int(self.__source.get_y()) - int(self.__destination.get_y()))

		self.__distance_travelled = horizontal_diff + vertical_diff

	def calculate_remaining_power(self):

		self.destination_direction_from_source()
		self.calculate_turns_taken()
		self.calculate_distance_travelled()

		power_spend = self.__distance_travelled * self.__travelling_power
		power_spend += self.__turns_taken * self.__turning_power

		return self.__power - power_spend

