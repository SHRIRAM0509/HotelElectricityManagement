from abc import ABC, abstractmethod
from typing import List

from models.device import Device
from models.device_not_found_exception import DeviceNotFoundException
from models.device_state import DeviceState
from models.device_type import DeviceType


MAIN_CORRIDOR_POWER_LIMIT = 15
SUB_CORRIDOR_POWER_LIMIT = 10
class Corridor(ABC):
	def __init__(self, id: int, devices: List[Device]):
		# TODO: check if device id is unique
		self.id = id
		self.devices_map = {device.id: device for device in devices}
		self.default_behaviour()
		
	def __getitem__(self, key: int) -> Device:
		if key in self.devices_map:
			return self.devices_map[key]
		raise DeviceNotFoundException(key)

	def toggle_device_status(self, device_id: int) -> None:
		device: Device = self.__getitem__(device_id)
		device.toggle_state()
	
	def set_device_state(self, device_id: int, device_state: DeviceState) -> None:
		device = self.__getitem__(device_id)
		device.set_state(device_state)
  
	def set_state_for_same_device_type(self, device_type: DeviceType, state: DeviceState):
		for device in self.devices_map.values():
			if device.is_of_type(device_type):
				device.set_state(state)
	
	def with_id(self, id: int):
		return self.id == id

	@property
	def power_consumption(self) -> int:
		return sum(device.power_consumption for device in self.devices_map.values())
  
	@abstractmethod
	def default_behaviour(self):
		pass

	@staticmethod
	@abstractmethod
	def power_limit(self) -> int:
		raise NotImplementedError

# assuming NightTimeSlot defaults, dont make default_behaviour abstract
class MainCorridor(Corridor):
	def default_behaviour(self):
		self.set_state_for_same_device_type(DeviceType.AC, DeviceState.ON)
		self.set_state_for_same_device_type(DeviceType.LIGHT, DeviceState.OFF)
	
	def power_limit(self) -> int:
		return MAIN_CORRIDOR_POWER_LIMIT

	def __str__(self) -> int:
		devices_status = ",".join(str(device) for device in self.devices_map.values())
		return f"Main Corridor {self.id}:- "

class SubCorridor(Corridor):
	def default_behaviour(self):
		self.set_state_for_same_device_type(DeviceType.AC, DeviceState.ON)
		self.set_state_for_same_device_type(DeviceType.LIGHT, DeviceState.OFF)

	def power_limit(self) -> int:
		return SUB_CORRIDOR_POWER_LIMIT
