import unittest

from models.device import Device
from models.device_state import DeviceState

class TestDevice(unittest.TestCase):
	def setUp(self):
		self.device = Device(5, 1)
		
	def test_if_device_state_is_initially_on(self):
		self.assertEqual(self.device.state, DeviceState.ON)
		
	def test_if_device_state_can_be_toggled(self):
		self.device.toggle_state()
		self.assertEqual(self.device.state, DeviceState.OFF)
		self.device.toggle_state()
		self.assertEqual(self.device.state, DeviceState.ON)

	def test_if_device_state_can_be_set(self):
		self.device.set_state(DeviceState.OFF)
		self.assertEqual(self.device.state, DeviceState.OFF)
		self.device.set_state(DeviceState.ON)
		self.assertEqual(self.device.state, DeviceState.ON)
  