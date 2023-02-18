from models.device_state import DeviceState
from models.device_type import DeviceType

class Device:
	__slots__ = ['type', 'power', 'id', 'state']

	def __init__(self, type: DeviceType, power: int, id: int, state: DeviceState = DeviceState.ON) -> None:
		self.type: DeviceType = type
		self.power: int = power
		self.id: int = id
		self.state: DeviceState = state
		# TODO: Is a uniq identifier needed?

	def toggle_state(self) -> None:
		self.state = DeviceState.OFF if self.state == DeviceState.ON else DeviceState.ON

	def set_state(self, state: DeviceState) -> None:
		self.state = state
  
	def is_of_type(self, type: DeviceType):
		return self.type == type

	@property
	def power_consumption(self) -> int:
		return self.power if self.is_on() else 0

	def is_on(self):
		return self.state == DeviceState.ON

	def __str__(self) -> str:
		return f"{self.type}: {self.state}"
