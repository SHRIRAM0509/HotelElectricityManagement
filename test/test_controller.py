import unittest

from models.controller import Controller
from models.corridor import Corridor, MainCorridor, SubCorridor
from models.device import Device
from models.device_type import DeviceType
from models.floor import Floor
from models.hotel import Hotel
from models.logger import ConsoleLogger
from models.rule import MotionDetectedRule, NightTimeSlotRule, PowerConsumptionLimitRule

class TestController(unittest.TestCase):
	def _get_AC_instance(self):
		return Device(DeviceType.AC, 10)
	
	def _get_light_instance(self):
		return Device(DeviceType.LIGHT, 5)

	def _get_main_corridor(self):
		devices = [self._get_AC_instance(), self._get_light_instance()]
		return MainCorridor(1, devices)
	
	def _get_sub_corridor(self):
		devices = [self._get_AC_instance(), self._get_light_instance()]
		return SubCorridor(1, devices)

	def _get_floor(self, number: int):
		main_corridor = self._get_main_corridor()
		sub_corridor1 = self._get_sub_corridor()
		sub_corridor2 = self._get_sub_corridor()
		return Floor(number, [main_corridor, sub_corridor1, sub_corridor2])

	def setUp(self) -> None:
		floors = [self._get_floor() for i in range(2)]
		self.hotel = Hotel(floors)
		rules = [
			NightTimeSlotRule,
			MotionDetectedRule,
			PowerConsumptionLimitRule
		]
		logger = ConsoleLogger()
		self.controller = Controller(self.hotel, rules, logger)
		self.controller.run()

