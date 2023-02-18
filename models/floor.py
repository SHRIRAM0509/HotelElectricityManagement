from typing import List
from models.corridor_not_found_exception import CorridorNotFoundException
from models.corridor import Corridor, MainCorridor, SubCorridor

class Floor:
	def __init__(self, number: int, corridors: List[Corridor]=list()) -> None:
		self.number = number
		self.corridors: List[Corridor] = corridors

	def get_corridor(self, corridor_id) -> Corridor:
		for corridor in self.corridors:
			if corridor.with_id(corridor_id):
				return corridor
		raise CorridorNotFoundException(corridor_id)

	def is_with_number(self, number: int):
		return self.number == number

	@property
	def power_consumption(self) -> int:
		return sum(corridor.power_consumption for corridor in self.corridors)

	@property
	def no_of_main_corridors(self) -> int:
		return sum(1 for corridor in self.corridors if isinstance(corridor, MainCorridor))

	@property
	def no_of_sub_corridors(self) -> int:
		return len(self.corridors) - self.no_of_main_corridors()

	@property
	def power_consumption_limit(self) -> int:
		main_corridor_power_limit = self.no_of_main_corridors * MainCorridor.power_limit()
		sub_corridor_power_limit = self.no_of_sub_corridors * SubCorridor.power_limit()
		return main_corridor_power_limit + sub_corridor_power_limit

	def __str__(self):
		return "\n".join(str(corridor) for corridor in self.corridors)

