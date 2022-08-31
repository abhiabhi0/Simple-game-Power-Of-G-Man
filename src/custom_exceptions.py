class InvalidInputFile(Exception):
	def __init__(self, msg="Invalid Input Format"):
		self.message = msg
		super().__init__(self.message)

class SourceNotPresent(Exception):
	def __init__(self, msg="Source not present in Input file"):
		self.msg = msg
		super().__init__(self.msg)

class DestinationNotPresent(Exception):
	def __init__(self, msg="Destination not present in Input file"):
		self.msg = msg
		super().__init__(self.msg)

class PrintCommandNotPresent(Exception):
	def __init__(self, msg="PRINT_POWER Command not present in Input file"):
		self.msg = msg
		super().__init__(self.msg)

class InvalidDirection(Exception):
	def __init__(self, msg="Invalid Direction in Input file"):
		self.msg = msg
		super().__init__(self.msg)

class InvalidSource(Exception):
	def __init__(self, msg="Invalid Source Format in Input file"):
		self.msg = msg
		super().__init__(self.msg)

class InvalidDestination(Exception):
	def __init__(self, msg="Invalid Destination Format in Input file"):
		self.msg = msg
		super().__init__(self.msg)