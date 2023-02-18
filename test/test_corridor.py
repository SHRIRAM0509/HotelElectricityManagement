import unittest
from models.corridor import Corridor
from models.corridor_type import CorridorType

from models.device import Device
from models.device_not_found_exception import DeviceNotFoundException
from models.device_state import DeviceState
from models.device_type import DeviceType

class TestCorridor(unittest.TestCase):
	def setUp(self) -> None:
		self.devices = [
			Device(DeviceType.LIGHT, 5, 1),
			Device(DeviceType.AC, 10, 2),
		]
		self.corridor = Corridor(CorridorType.MAIN_CORRIDOR, self.devices)
	
	def test_if_no_devices_is_right(self):
		devices_in_corridor = self.corridor._devices_map
		self.assertEqual(len(devices_in_corridor.keys()), 2)
  
	def test_for_device_existence(self):
		key = 3
		with self.assertRaises(DeviceNotFoundException):
			self.corridor[key]
   	
	def test_if_device_state_can_be_toggled(self):
		key = 1
		self.corridor.toggle_device_status(key)
		self.assertEqual(self.corridor[key].state, DeviceState.OFF)
	
	def test_if_device_status_can_be_set(self):
		key = 1
		self.corridor.set_device_state(key, DeviceState.ON)
		self.assertEqual(self.corridor[key].state, DeviceState.ON)