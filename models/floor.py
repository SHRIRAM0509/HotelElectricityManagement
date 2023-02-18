from typing import List
from models.corridor import Corridor


class Floor:
	def __init__(self, number: int, corridors: List[Corridor]=list()) -> None:
		self.number = number
		self.corridors = corridors
