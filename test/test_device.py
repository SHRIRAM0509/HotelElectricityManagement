import unittest

from models.device import Device
from models.device_state import DeviceState

class TestDevice(unittest.TestCase):
    def setUp(self):
        self.device = Device(5)
        
    def test_if_device_state_is_initially_on(self):
        self.assertEquals(self.device.state, DeviceState.ON)
        
	