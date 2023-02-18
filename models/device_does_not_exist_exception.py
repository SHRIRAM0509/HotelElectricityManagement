class DeviceDoesNotExistException(Exception):
	def __init__(self, id: int) -> None:
		super().__init__(f"Device with {id} doesn't exist")
