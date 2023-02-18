class FloorNotFoundException(Exception):
	def __init__(self, id: int) -> None:
		super().__init__(f"Floor {id} doesn't exist")
  