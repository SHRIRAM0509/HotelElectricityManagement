import unittest

from models.device import Device
from models.device_state import DeviceState

class TestDevice(unittest.TestCase):
	def setUp(self):
		self.device = Device(5)
		
	def test_if_device_state_is_initially_on(self):
		self.assertEqual(self.device.state, DeviceState.ON)
		
	def test_if_device_state_can_be_toggled(self):
		self.device.toggleState()
		self.assertEqual(self.device.state, DeviceState.OFF)
		self.device.toggleState()
		self.assertEqual(self.device.state, DeviceState.ON)

	