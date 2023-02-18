import unittest
from models.corridor import Corridor

from models.device import Device
from models.device_does_not_exist_exception import DeviceDoesNotExistException
from models.device_state import DeviceState

class TestCorridor(unittest.TestCase):
	def setUp(self) -> None:
		self.devices = [
			Device(5, 1),
			Device(10, 2),
		]
		self.corridor = Corridor(self.devices)
	
	def test_if_no_devices_is_right(self):
		devices_in_corridor = self.corridor.devices
		self.assertEqual(len(devices_in_corridor.keys()), 2)
  
	def test_for_device_existence(self):
		key = 3
		with self.assertRaises(DeviceDoesNotExistException):
			self.corridor[key]
   	
	def test_if_device_state_can_be_toggled(self):
		key = 1
		self.corridor.toggle_device_status(key)
		self.assertEqual(self.corridor[key].state, DeviceState.OFF)
	
	def test_if_device_status_can_be_set(self):
		key = 1
		self.corridor.set_device_state(key, DeviceState.ON)
		self.assertEqual(self.corridor[key].state, DeviceState.ON)