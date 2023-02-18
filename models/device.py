from models.device_state import DeviceState

class Device:
	__slots__ = ['power', 'state']

	def __init__(self, power: int, state: DeviceState = DeviceState.ON) -> None:
		self.power: int = power
		self.state: DeviceState = state
		# TODO: Is a uniq identifier needed?

	def toggleState(self) -> None:
		self.state = DeviceState.OFF if self.state == DeviceState.ON else DeviceState.ON
