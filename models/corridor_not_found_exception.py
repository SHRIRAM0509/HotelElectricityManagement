class CorridorNotFoundException(Exception):
	def __init__(self, id: int) -> None:
		super().__init__(f"Corridor {id} doesn't exist")
  