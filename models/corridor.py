from typing import List
from models.corridor_type import CorridorType
from models.device import Device
from models.device_not_found_exception import DeviceNotFoundException
from models.device_state import DeviceState
from models.device_type import DeviceType

class Corridor:
	def __init__(self, type: CorridorType, devices: List[Device]):
		# TODO: check if device id is unique
		self.type = type
		self._devices_map = {device.id: device for device in devices}
		
	def __getitem__(self, key: int) -> Device:
		if key in self._devices_map:
			return self._devices_map[key]
		raise DeviceNotFoundException(key)

	def toggle_device_status(self, device_id: int) -> None:
		device: Device = self.__getitem__(device_id)
		device.toggle_state()
	
	def set_device_state(self, device_id: int, device_state: DeviceState) -> None:
		device = self.__getitem__(device_id)
		device.set_state(device_state)
  
	def toggle_all_device_type(self, device_type: DeviceType):
		for device in self._devices_map.values():
			if device.is_of_type(type):
				device.toggle_state()
	
	def is_of_type(self, type: CorridorType):
		return self.corridor_type == type
