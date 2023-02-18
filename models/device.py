from models.device_state import DeviceState

class Device:
	__slots__ = ['power', 'id', 'state']

	def __init__(self, power: int, id: int, state: DeviceState = DeviceState.ON) -> None:
		self.power: int = power
		self.id: int = id
		self.state: DeviceState = state
		# TODO: Is a uniq identifier needed?

	def toggle_state(self) -> None:
		self.state = DeviceState.OFF if self.state == DeviceState.ON else DeviceState.ON

	def set_state(self, state: DeviceState) -> None:
		self.state = state
