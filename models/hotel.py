from typing import List
from models.floor import Floor

class Hotel:
	def __init__(self, floors: List[Floor]=list()) -> None:
		self.floors = floors

