from typing import List
from models.floor import Floor
from models.floor_not_found_exception import FloorNotFoundException

class Hotel:
	def __init__(self, floors: List[Floor]=list()) -> None:
		self.floors = floors

	def __getitem__(self, idx: int) -> Floor:
		for floor in self.floors:
			if floor.is_with_number(idx):
				return floor
		raise FloorNotFoundException(idx)

