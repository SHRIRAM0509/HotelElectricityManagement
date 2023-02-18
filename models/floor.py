from typing import Callable, List
from models.corridor import Corridor
from models.corridor_type import CorridorType


class Floor:
	def __init__(self, number: int, corridors: List[Corridor]=list()) -> None:
		self.number = number
		self.corridors: List[Corridor] = corridors

	def get_corridors_by_type(self, corridor_type: CorridorType) -> List[Corridor]:
		return [ corridor.is_of_type(corridor_type) for corridor in self.corridors ]

	def is_with_number(self, number: int):
		return self.number == number

