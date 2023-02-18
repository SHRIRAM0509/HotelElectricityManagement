from typing import List
from models.hotel import Hotel
from models.rule import Rule
from models.logger import Logger

class Controller:
	def __init__(self, hotel: Hotel, rules: List[type], logger: Logger) -> None:
		self.hotel = hotel
		self.rules = rules
		self.logger = logger
  
	def run(self):
		for rule in self.rules:
			rule(self.hotel, self.rules).run()
		self.logger.log(str(self.hotel))

